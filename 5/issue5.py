from what_is_year_now import what_is_year_now
import pytest

import urllib.request
from unittest.mock import patch
from io import StringIO


@pytest.mark.parametrize(
    "sample_date, sample_year",
    [
        ('16.05.2000', 2000),
        ('01.01.0001', 1),
        ('24.02.2022', 2022),
        ('23.12.2022', 2022),
        ('0988-06-01', 988),
        ('1952-10-07', 1952),
        ('6999-01-01', 6999),
    ],
)
def test_date_format(sample_date, sample_year):
    with patch.object(urllib.request, "urlopen") as mock_urlopen:
        url_str = f'{{"currentDateTime": "{sample_date}"}}'
        mock_urlopen.return_value = StringIO(url_str)
        assert what_is_year_now() == sample_year


def test_incorrect_format():
    date = StringIO('{"currentDateTime": "23/12/2022"}')
    with patch.object(urllib.request, "urlopen", return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_incorrect_empty():
    date = StringIO('')
    with patch.object(urllib.request, "urlopen", return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_not_date():
    date = StringIO('10 o`clock')
    with patch.object(urllib.request, "urlopen", return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()
