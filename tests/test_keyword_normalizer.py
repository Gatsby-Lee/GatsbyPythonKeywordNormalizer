# -*- coding: utf-8 -*-


def test_replace_special_char():
    from gatsby_normalizer.keyword_normalizer import _replace_special_char
    assert _replace_special_char('abc#', ['#', '!']) == 'abc'


def test_():
    from gatsby_normalizer import normalize_searchterm

    assert normalize_searchterm('ABC ') == 'abc'
    assert normalize_searchterm('A  B C') == 'a b c'
    assert normalize_searchterm('A  B\tC') == 'a b c'
    assert normalize_searchterm('A  B\nC') == 'a b c'
    assert normalize_searchterm('     A  B  \nC   ') == 'a b c'
