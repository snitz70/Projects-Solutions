import pytest
import count


def test_count_vowels():
    assert count.vowels('this is a test') == 4


def test_count_no_vowels():
    assert count.vowels('dfghjklmn') == 0


def test_count_all_vowels():
    assert count.vowels('aeiou') == 5


def test_count_vowel_frequency():
    assert count.vowel_frequency('this is a test')['i'] == 2


def test_make_sure_only_vowels_are_returned():
    with pytest.raises(KeyError):
        count.vowel_frequency('this is a test')['t']
