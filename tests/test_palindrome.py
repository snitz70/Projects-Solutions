import palindrome


def test_if_palindrome():
    assert palindrome.palindrome('racecar')


def test_not_palindrome():
    assert not palindrome.palindrome('brian')


def test_palindrome_full_sentence():
    assert palindrome.palindrome('A Man, A Plan, A Canal-Panama!')
