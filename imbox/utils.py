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


def str_decode(
    value: str, encoding: Optional[str] = None, errors: str = "strict"
) -> str:
    """
    Decode a value from bytes or str to str.

    Args:
        value: The value to decode.
        encoding: The encoding to use (default is None).
        errors: The error handling scheme (default is 'strict').

    Returns:
        The decoded string.

    Raises:
        TypeError: If the value is not a bytes or str object.
    """
    if isinstance(value, str):
        return _decode_from_str(value, encoding, errors)
    elif isinstance(value, bytes):
        return _decode_from_bytes(value, encoding, errors)
    else:
        raise TypeError("Cannot decode '{}' object".format(value.__class__))


def _decode_from_str(
    value: str, encoding: Optional[str] = None, errors: str = "strict"
) -> str:
    encoded_bytes = bytes(value, encoding, errors)
    return encoded_bytes.decode("utf-8")


def _decode_from_bytes(
    value: bytes, encoding: Optional[str] = None, errors: str = "strict"
) -> str:
    return value.decode(encoding or "utf-8", errors=errors)


def date_to_date_text(date):
    """Return a date in the RFC 3501 date-text syntax"""
    tzutc = datetime.timezone.utc
    dt = datetime.datetime.combine(date, datetime.time.min, tzutc)
    return Time2Internaldate(dt)[1:12]
