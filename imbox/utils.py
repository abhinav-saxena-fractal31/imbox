import datetime
import logging
from imaplib import Time2Internaldate
from typing import Optional
logger = logging.getLogger(__name__)


def str_encode(
    value: str, encoding: Optional[str] = None, errors: str = "strict"
) -> str:
    """
    Encodes a string using the specified encoding.

    Args:
        value: The string to encode.
        encoding: The encoding to use. If None, the default encoding is used.
        errors: The error handling scheme to use. Defaults to 'strict'.

    Returns:
        The encoded string.

    Raises:
        UnicodeEncodeError: If the string cannot be encoded with the specified encoding and error handling scheme.

    Example:
        >>> str_encode('hello')
        'hello'
        >>> str_encode('hello', encoding='utf-8')
        'hello'
        >>> str_encode('привет', encoding='ascii', errors='replace')
        '??????'
    """
    logger.debug(
        f"Encode string '{value}' with encoding '{encoding}' and errors '{errors}'"
    )
    return str(value.encode(encoding, errors))


def str_decode(value='', encoding=None, errors='strict'):
    if isinstance(value, str):
        return bytes(value, encoding, errors).decode('utf-8')
    elif isinstance(value, bytes):
        return value.decode(encoding or 'utf-8', errors=errors)
    else:
        raise TypeError("Cannot decode '{}' object".format(value.__class__))


def date_to_date_text(date):
    """Return a date in the RFC 3501 date-text syntax"""
    tzutc = datetime.timezone.utc
    dt = datetime.datetime.combine(date, datetime.time.min, tzutc)
    return Time2Internaldate(dt)[1:12]
