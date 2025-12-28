import pytest
from main import isMatch

'''
run test with command:
pytest -vv .\test_isMatch.py
'''


class TestTinyInputs:
    @pytest.mark.parametrize(
        "pattern,string,expected",
        [
            ("", "", True),
            ("", "a", False),
            ("a", "a", True),
            ("a", "", False),
            (".", "", False),
            (".", "a", True)
        ],
    )
    def test_literals(self, pattern, string, expected):
        assert isMatch(string, pattern) == expected


class TestLiteralMatching:
    @pytest.mark.parametrize(
        "pattern,string,expected",
        [
            ("abc", "abc", True),
            ("abc", "acb", False),
            ("abc", "abcd", False),
            ("abc", "ab", False)
        ],
    )
    def test_literals(self, pattern, string, expected):
        assert isMatch(string, pattern) == expected


class TestDotOperator:
    @pytest.mark.parametrize(
        "pattern,string,expected",
        [
            ("abc.", "abcd", True),
            ("abc.", "abcde", False),
            ("abc.e", "abcze", True),
            ("abc.e", "abcdf", False)
        ],
    )
    def test_dot(self, pattern, string, expected):
        assert isMatch(string, pattern) == expected


class TestRepetitionOperator:
    @pytest.mark.parametrize(
        "pattern, string, expected",
        [
            ("a*", "", True),
            ("ab*", "a", True),
            ("ab*", "bbbb", False),
            ("ab*", "ab", True),
            ("ab*", "abbbb", True),
            ("ab*", "abbbc", False),
            ("a.*", "a", True),
            ("a.*", "bbbb", False),
            ("a.*", "ab", True),
            ("a.*", "abbbb", True),
            ("a.*", "abcde", True)
        ]
    )
    def test_repetition_no_suffix(self, pattern, string, expected):
        assert isMatch(string, pattern) == expected

    @pytest.mark.parametrize(
        "pattern, string, expected",
        [
            ("a.*b", "ab", True),
            ("a.*b", "azzzz", False),
            ("a.*b", "axyzb", True),
            ("a.*b", "azzzbz", False),
            ("a.*b", "abbbb", True),
            ("a.*b.*c", "abc", True),
            ("a.*b.*c", "azbzc", True),
            ("a.*b.*c", "azbzcz", False),
            ("a.*b.*c", "abbbccc", True),
            ("a*b", "a", False),
            ("a*b", "ab", True),
            ("a*b", "aaab", True),
            ("a*b", "azzb", False),
        ]
    )
    def test_repetition_with_suffix(self, pattern, string, expected):
        assert isMatch(string, pattern) == expected
