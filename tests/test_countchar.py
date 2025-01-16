import pytest

from countchar.count_char import count_char

def test_count_char():

    string = "hello"
    expected = 5
    actual = count_char(string)
    assert actual == expected

    string = ""
    expected = 0
    actual = count_char(string)
    assert actual == expected

    string = "Python is cool"
    expected = 14
    actual = count_char(string)
    assert actual == expected

def test_count_char_wrong_input():
    with pytest.raises(TypeError):
        count_char(123)
