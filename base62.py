# -*- coding: utf-8 -*-
"""
base62
~~~~~~
Originated from http://blog.suminb.com/archives/558
"""

__title__ = 'base62'
__author__ = 'Sumin Byeon'
__email__ = 'suminb@gmail.com'
__version__ = '0.4.0'

BASE = 62
CHARSET_DEFAULT = (
	'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
)
CHARSET_INVERTED = (
	'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
)


def bytes_to_int(s, byteorder='big', signed=False):
	"""Converts a byte array to an integer value.
	Python 3 comes with a built-in function to do this, but we would like to
	keep our code Python 2 compatible.
	"""

	try:
		return int.from_bytes(s, byteorder, signed=signed)
	except AttributeError:
		# For Python 2.x
		if byteorder != 'big' or signed:
			raise NotImplementedError()

		# NOTE: This won't work if a generator is given
		n = len(s)
		ds = (x << (8 * (n - 1 - i)) for i, x in enumerate(bytearray(s)))

		return sum(ds)


def encode(n, charset=CHARSET_DEFAULT):
	"""Encodes a given integer ``n``."""

	chs = []
	while n > 0:
		r = n % 62
		n //= 62
		chs = [charset[r]] + chs

	if len(chs) == 0: return "0"
	return ''.join(chs)

def encodebytes(s, charset=CHARSET_DEFAULT):
	"""Encodes a bytestring into a base62 string.
	:param s: A byte array
	"""

	_check_bytes_type(s)
	return encode(bytes_to_int(s), charset=charset)


def decode(b, charset=CHARSET_DEFAULT):
    """Decodes a base62 encoded value ``b``."""

	l, i, v = len(b), 0, 0
	for x in b:
		v += charset.index(x) * (62 ** (l - (i + 1)))
		i += 1

	return v


def decodebytes(s, charset=CHARSET_DEFAULT):
	"""Decodes a string of base62 data into a bytes object.
	:param s: A string to be decoded in base62
	:rtype: bytes
	"""

	decoded = decode(s, charset=charset)
	buf = bytearray()
	while decoded > 0:
		buf.append(decoded & 0xff)
		decoded //= 256
	buf.reverse()

	return bytes(buf)


def _value(ch, charset):
	"""Decodes an individual digit of a base62 encoded string."""

	try:
		return charset.index(ch)
	except ValueError:
		raise ValueError('base62: Invalid character (%s)' % ch)


def _check_bytes_type(s):
	"""Checks if the input is in an appropriate type."""

	if not isinstance(s, bytes):
		msg = 'expected bytes-like object, not %s' % s.__class__.__name__
		raise TypeError(msg)
