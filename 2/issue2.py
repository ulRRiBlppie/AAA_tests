import pytest
from morse import decode


@pytest.mark.parametrize('s,exp', [
    ('... --- ...', 'SOS'),
    ('... --- ...', 'sos'),
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('-- . .-. .-. -.--', 'MERRY'),
    ('-.-. .... .-. .. ... - -- .- ...', 'CHRISTMAS'),
    ('.---- ..--- ...-- ', '123')
])
def test_decode(s, exp):
    assert decode(s) == exp