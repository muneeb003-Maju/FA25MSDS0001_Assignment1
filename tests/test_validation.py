from src.FA25MSDS0001.utils.validation import validate_name
from src.FA25MSDS0001.utils.validation import validate_marks


def test_valid_name():
    assert validate_name("Ali") is True


def test_empty_name():
    assert validate_name("") is False


def test_valid_marks():
    assert validate_marks(85) is True


def test_negative_marks():
    assert validate_marks(0 - 10) is False


def test_marks_above_limit():
    assert validate_marks(150) is False