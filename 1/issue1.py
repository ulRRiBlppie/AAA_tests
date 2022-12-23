from morse import encode
import doctest


def encode_test(message):
    """
    >>> encode_test('SOS')
    '... --- ...'
    >>> encode_test('sos')
    Traceback (most recent call last):
    KeyError: 's'
    >>> encode_test(1)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable

    >>> encode_test('S O S') # doctest: +NORMALIZE_WHITESPACE
    '... --- ...'
    >>> encode_test('SOOOOOOOOOOS') # doctest: +ELLIPSIS
    '... ... ...'
    >>> encode_test('S OOOOOOOO S') # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    '... ... --- ... ...'
    """

    return encode(message)


if __name__ == '__main__':
    doctest.testmod()
