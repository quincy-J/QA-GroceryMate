import pytest
from Testautomatisierung.src.count_word_matches import count_word_matches


# -------------------------
# ÜBUNG 1 – BASIS-TESTS
# -------------------------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("Hello world", "world", 1),
        ("hello hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ],
)
def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected


# -------------------------
# ÜBUNG 2 – EDGE CASES
# -------------------------
@pytest.fixture
def edge_case_inputs():
    return [
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0),
        ("hello   world", "world", 1),
        (" cat ", "cat", 1),
        ("cat,dog cat", "cat", 1),
        ("x y z", "x", 1),
    ]


def test_count_word_matches_edge_cases(edge_case_inputs):
    for text, target, expected in edge_case_inputs:
        assert count_word_matches(text, target) == expected


# -------------------------
# ÜBUNG 3 – NEGATIVE TESTS
# -------------------------
@pytest.fixture
def invalid_inputs():
    return [
        (None, "word", 0),
        ("hello world", None, 0),
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError),
    ]


def test_count_word_matches_invalid_inputs(invalid_inputs):
    for text, target, expected in invalid_inputs:
        if expected == 0:
            assert count_word_matches(text, target) == 0
        else:
            with pytest.raises(expected):
                count_word_matches(text, target)