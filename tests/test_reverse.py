import reverse


def test_reverse_string():
    assert reverse.reverse_str('brian') == 'nairb'

def test_reverse_sentence():
    assert reverse.reverse_str('this is a test') == 'tset a si siht'
