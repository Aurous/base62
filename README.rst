base62
======

A Python module for ``base62`` encoding. Forked from https://github.com/suminb/base62

Rationale
---------

When writing a web application, often times we would like to keep the URLs short.

::

    http://localhost/post/V1Biicwt

This certainly gives a more concise look than the following.

::

    http://localhost/post/109237591284123

This was the original motivation to write this module, but there shall be much
more broader potential use cases of this module. The main advantage of
``base62`` is that it is URL-safe (as opposed to ``base64``) due to the lack of
special characters such as '``/``' or '``=``'. Another key aspect is that the
alphabetical orders of the original (unencoded) data is preserved when encoded.
In other words, encoded data can be sorted without being decoded at all.

Installation
============
::

    git clone https://github.com/aurous/base62
    cd base62 && python setup.py install

Usage
=====

The following section describes a basic usage of ``base62``.

.. code:: python

    >>> import base62

    >>> base62.encode(34441886726)
    'base62'

    >>> base62.decode('base62')
    34441886726

From version ``0.2.0``, ``base62`` supports ``bytes`` array encoding as well.

.. code:: python

    >>> base62.encodebytes(b'\0')
    0

    >>> base62.encodebytes(b'\xff\xff')
    H31

    >>> base62.decodebytes('0')
    b''

    >>> base62.decodebytes('1')
    b'\x01'

Tests
=====

You may run some test cases to ensure all functionalities are operational.

::

    py.test -v

If ``pytest`` is not installed, you may want to run the following commands:

::

    pip install -r tests/requirements.txt

