# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import datetime
from functools import total_ordering
import json
import re
import sys
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


DEFAULT_HOST = "https://crash-stats.mozilla.org"


class JsonDTEncoder(json.JSONEncoder):
    """JSON encoder that handles datetimes

    >>> json.dumps(some_data, cls=JsonDTEncoder)
    ...

    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S.%f")
        return json.JSONEncoder.default(self, obj)


class WrappedTextHelpFormatter(argparse.HelpFormatter):
    """Subclass that wraps description and epilog text taking paragraphs into account"""

    def _fill_text(self, text, width, indent):
        """Wraps text like HelpFormatter, but doesn't squash lines

        This makes it easier to do lists and paragraphs.

        """
        parts = text.split("\n\n")
        for i, part in enumerate(parts):
            # Check to see if it's a bulleted list--if so, then fill each line
            if part.startswith("* "):
                subparts = part.split("\n")
                for j, subpart in enumerate(subparts):
                    subparts[j] = super(WrappedTextHelpFormatter, self)._fill_text(
                        subpart, width, indent
                    )
                parts[i] = "\n".join(subparts)
            else:
                parts[i] = super(WrappedTextHelpFormatter, self)._fill_text(
                    part, width, indent
                )

        return "\n\n".join(parts)


class FlagAction(argparse.Action):
    """Facilitates --flag, --no-flag arguments

    Usage::

        parser.add_argument(
            '--flag', '--no-flag', action=FlagAction, default=True,
            help='whether to enable flag'
        )


    Which allows you to do::

        $ command
        $ command --flag
        $ command --no-flag


    And the help works nicely, too::

        $ command --help
        ...
        optional arguments:
           --flag, --no-flag  whether to enable flag

    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        # Validate option strings--we should have a no- option for every option
        options = [opt.strip("-") for opt in option_strings]

        yes_options = [opt for opt in options if not opt.startswith("no-")]
        no_options = [opt[3:] for opt in options if opt.startswith("no-")]

        if sorted(yes_options) != sorted(no_options):
            raise ValueError("There should be one --no option for every option value.")

        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if option_string.startswith("--no"):
            value = False
        else:
            value = True
        setattr(namespace, self.dest, value)


class FallbackToPipeAction(argparse.Action):
    """Fallback to load strings piped from stdin

    This action reads from stdin when the positional arguments were omitted. It
    expects one value per line, and at least one value.

    This does not work with named arguments, since the action is not called
    when a named argument is omitted.

    To use this as a fallback for positional arguments:
    > parser.add_argument('name', nargs='*', action=FallbackToPipeAction)
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        """Initialize the FallbackToPipeAction.

        :param option_strings: Names for non-positional arguments.
        :param dest: The destination attribute on the parser
        :param nargs: The number of arguments, must be '*' for zero or more
        :param kwargs: Additional parameters for the parser argument
        """
        if option_strings:
            raise ValueError("This action does not work with named arguments")
        if nargs != "*":
            # For nargs='*', the action is called with an empty list.
            # For other values ('?', '+', 1), the action isn't called, so we
            # can't fallback to reading from stdin.
            raise ValueError("nargs should be '*'")
        super().__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        """Call the FallbackToPipeAction.

        If the arguments were set on the command line, use them. Otherwise,
        try reading from stdin (the pipe). If a pipe was not provided or was
        empty, parser.error is called to print usage and exit early.

        :param parser: The argument parser
        :param namespace: The destination namespace
        :param values: The parsed values, an empty list if omitted
        :param option_string: The option name, or None for positional arguments
        """

        if not values:
            if sys.stdin.isatty():
                # There is no data being piped to the script, but instead it
                # is an interactive TTY. Instead of blocking while waiting
                # for input, exit on the missing parameter
                parser.error(
                    'argument "%s" was omitted and stdin is not a pipe.' % self.dest
                )
            else:
                # Data is being piped to this script. Remove trailing newlines
                # from reading sys.stdin as line iterator.
                type_func = self.type or str
                values = [type_func(item.rstrip()) for item in sys.stdin]
                if not values:
                    parser.error(
                        'argument "%s" was omitted and stdin was empty.' % self.dest
                    )

        setattr(namespace, self.dest, values)


class HTTPAdapterWithTimeout(HTTPAdapter):
    """HTTPAdapter with a default timeout

    This allows you to set a default timeout when creating the adapter.
    It can be overridden here as well as when doing individual
    requests.

    :arg varies default_timeout: number of seconds before timing out

        This can be a float or a (connect timeout, read timeout) tuple
        of floats.

        Defaults to 5.0 seconds.

    """

    def __init__(self, *args, **kwargs):
        self._default_timeout = kwargs.pop("default_timeout", 5.0)
        super().__init__(*args, **kwargs)

    def send(self, *args, **kwargs):
        # If there's a timeout, use that. Otherwise, use the default.
        kwargs["timeout"] = kwargs.get("timeout") or self._default_timeout
        return super().send(*args, **kwargs)


def session_with_retries(
    total_retries=5,
    backoff_factor=0.2,
    status_forcelist=(429, 500),
    default_timeout=5.0,
):
    """Returns session that retries on HTTP 429 and 500 with default timeout

    :arg int total_retries: total number of times to retry

    :arg float backoff_factor: number of seconds to increment by between
        attempts

        For example, 0.1 will back off 0.1s, then 0.2s, then 0.3s, ...

    :arg tuple of HTTP codes status_forcelist: tuple of HTTP codes to
        retry on

    :arg varies default_timeout: number of seconds before timing out

        This can be a float or a (connect timeout, read timeout) tuple
        of floats.

    :returns: a requests Session instance

    """
    retries = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=list(status_forcelist),
    )

    session = requests.Session()

    # Set the User-Agent header so we can distinguish our stuff from other stuff
    session.headers.update({"User-Agent": "crashstats-tools/1.0"})

    adapter = HTTPAdapterWithTimeout(
        max_retries=retries, default_timeout=default_timeout
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


class BadRequest(Exception):
    """HTTP Request is not valid."""


class BadAPIToken(Exception):
    """API Token is not valid."""


def http_get(url, params, api_token=None):
    """Retrieve data at url with params and api_token.

    :raises CrashDoesNotExist:
    :raises BadAPIToken:

    :returns: requests Response

    """
    if api_token:
        headers = {"Auth-Token": api_token}
    else:
        headers = {}

    session = session_with_retries()

    resp = session.get(url, params=params, headers=headers)

    # Handle 403 so we can provide the user more context
    if api_token and resp.status_code == 403:
        raise BadAPIToken(resp.json().get("error", "No error provided"))

    # Handle 400 which indicates a problem with the request
    if resp.status_code == 400:
        raise BadRequest(resp.json().get("error", "No error provided"))

    # Raise an error for any other non-200 response
    resp.raise_for_status()
    return resp


def http_post(url, data, api_token=None):
    """POST data at url with api_token.

    :raises BadAPIToken:

    :returns: requests Response

    """
    if api_token:
        headers = {"Auth-Token": api_token}
    else:
        headers = {}

    session = session_with_retries()

    resp = session.post(url, data=data, headers=headers)

    # Handle 403 so we can provide the user more context
    if api_token and resp.status_code == 403:
        raise BadAPIToken(resp.json().get("error", "No error provided"))

    # Raise an error for any other non-200 response
    resp.raise_for_status()
    return resp


@total_ordering
class Infinity(object):
    """Infinity is greater than anything else except other Infinities

    NOTE(willkg): There are multiple infinities and not all infinities are
    equal, so what we're doing here is wrong, but it's helpful. We can rename
    it if someone gets really annoyed.

    """

    def __eq__(self, obj):
        return isinstance(obj, Infinity)

    def __lt__(self, obj):
        return False

    def __repr__(self):
        return "Infinity"

    def __sub__(self, obj):
        if isinstance(obj, Infinity):
            return 0
        return self

    def __rsub__(self, obj):
        # We don't need to deal with negative infinities, so let's not
        raise ValueError("This Infinity does not support right-hand-side")


# For our purposes, there is only one infinity
INFINITY = Infinity()


class InvalidArg(Exception):
    pass


def parse_args(args):
    """Convert command line arguments to supersearch arguments."""
    params = {}

    while args:
        field = args.pop(0)
        if not field.startswith("--"):
            raise InvalidArg("unknown argument %r" % field)
            return 1

        if "=" in field:
            field, value = field.split("=", 1)
        else:
            if args:
                value = args.pop(0)
            else:
                raise InvalidArg("arg %s has no value" % field)

        # Remove the -- from the beginning of field
        field = field[2:]

        # Remove quotes from value if they exist
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        params.setdefault(field, []).append(value)
    return params


CRASH_ID_RE = re.compile(
    r"""
    ^
    [a-f0-9]{8}-
    [a-f0-9]{4}-
    [a-f0-9]{4}-
    [a-f0-9]{4}-
    [a-f0-9]{6}
    [0-9]{6}      # date in YYMMDD
    $
""",
    re.VERBOSE,
)


def is_crash_id_valid(crash_id):
    """Returns whether this is a valid crash id

    :arg str crash_id: the crash id in question

    :returns: True if it's valid, False if not

    """
    return bool(CRASH_ID_RE.match(crash_id))


def parse_crashid(item):
    """Returns a crashid from a number of formats.

    This handles the following three forms of crashids:

    * CRASHID
    * bp-CRASHID
    * http[s]://HOST[:PORT]/report/index/CRASHID

    :arg str item: the thing to parse a crash id from

    :returns: crashid as str or None

    """
    if is_crash_id_valid(item):
        return item

    if item.startswith("bp-") and is_crash_id_valid(item[3:]):
        return item[3:]

    if item.startswith("http"):
        parsed = urlparse(item)
        path = parsed.path
        if path.startswith("/report/index"):
            crash_id = path.split("/")[-1]
            if is_crash_id_valid(crash_id):
                return crash_id
