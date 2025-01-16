import pytest

from countchar.count_char import count_char


@pytest.mark.parametrize(
    "test_data_line_num, expected_count",
    [
        (0, 34),
        (1, 10),
        (2, 7)
    ]
)
def test_count_char_file_n(text_data, test_data_line_num, expected_count):
    string = text_data[test_data_line_num].strip()
    expected = expected_count
    actual = count_char(string)
    assert actual == expected
