from strings import pig_latin


def test_return_pig_latin_single_word():
    assert pig_latin.convert_to('brian') == 'ianbray'
    assert pig_latin.convert_to('egg') == 'eggway'


def test_return_pig_latin_full_sentence():
    assert pig_latin.convert_to('this is a test') == 'isthay isway away esttay'
