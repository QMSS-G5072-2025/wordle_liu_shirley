from wordle_xl3572 import wordle_xl3572


import pytest


# Word list for testing
WORD_LIST = [
    "crane", "apple", "hello", "world", "python",
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]


# =============================================================================
# PART 1: BASIC TESTING
# =============================================================================
# Note: Each test function can contain multiple related assertions.
# This is standard practice - you're testing the same function with different
# inputs to verify it handles various scenarios correctly.

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.

    TODO: Students should implement this test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """

    examples = [
        # Valid guesses (correct length, lowercase, alphabetic)
        ("crane", True),
        ("apple", True),
        ("hello", True),
        ("world", True),

        # Invalid guesses (wrong length, uppercase, non-alphabetic)
        ("python", False),
        ("cra", False),
        ("CRANE", False),
        ("Crane", False),
        ("cr4ne", False),
        ("crane!", False),
        # Edge cases (empty string, None, non-string inputs)
        ("", False),
        (None, False),
        (12345, False),
    ]

    # TODO: Implement your test cases here
    for example, expected in examples:
        result = validate_guess(example)
        assert result == expected, f"Expected {expected}, got {result}"


def test_check_guess_basic():
    """
    Test basic check_guess functionality.

    TODO: Students should implement this test function with:
    - Perfect match (all green)
    - No matches (all gray)
    - Mixed results (green, yellow, gray combinations)
    - Edge cases (different lengths)

    Remember: Run check_guess() with different inputs first to see what it returns!
    """

    examples = [
        # Perfect match (all green)
        ("crane", "crane", [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),
        # No matches (all gray)
        ("crane", "blimp", [('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')]),
        # Mixed results (green, yellow, gray combinations)
        ("crane", "react", [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]),
        # Edge cases (different lengths)
        ("crane", "too", []),
        ("apple", "app", [])
    ]

    # TODO: Implement your test cases here
    for secret, guess, expected in examples:
        result = check_guess(secret, guess)
        assert result == expected, f"Expected {expected}, got {result}"


def test_is_valid_word():
    """
    Test the is_valid_word function.

    TODO: Students should implement this test function with:
    - Valid words (case insensitive)
    - Invalid words (not in list)
    - Edge cases (empty string, empty word list)
    """
    examples = [
        # Valid words (case in-sensitive)
        ("crane", True),
        ("apple", True),
        ("HELLO", True),
        ("World", True),
        # Invalid words (not in list)
        ("orange", False),
        ("tree", False),
        # Edge cases (empty string, empty word list)
        ("", False)
    ]

    for word, expected in examples:
        result = is_valid_word(word, WORD_LIST)
        assert result == expected, f"Expected {expected}, got {result}"

    # empty word list
    empty_list_example = [("crane", False)]
    empty_list = []
    for word, expected in empty_list_example:
        result = is_valid_word(word, empty_list)
        assert result == expected, f"Expected {expected}, got {result}"


# =============================================================================
# PART 2: ADVANCED TESTING
# =============================================================================

@pytest.mark.parametrize("secret_word,guess,expected", [
    # TODO: Students should add 5-6 test cases here

    ("crane", "crane", [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),
    # No matches(all gray)
    ("crane", "blimp", [('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')]),
    # Mixed results (green, yellow, gray combinations)
    ("crane", "react", [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]),
    # Duplicate letters in guess
    ("apple", "paper", [('p', 'yellow'), ('a', 'yellow'), ('p', 'green'), ('e', 'yellow'), ('r', 'gray')]),
    # all yellow
    ("crane", "nacer", [('n', 'yellow'), ('a', 'yellow'), ('c', 'yellow'), ('e', 'yellow'), ('r', 'yellow')])
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    """
    Test check_guess with multiple scenarios using parametrize.

    This test will run once for each set of parameters you provide above.
    """

    result = check_guess(secret_word, guess)
    assert result == expected, f"Failed for {secret_word} vs {guess}. Expected {expected}, got {result}"


@pytest.fixture
def common_word_list():
    """
    Fixture providing a list of common 5-letter words.

    TODO: Students should implement this fixture by returning a word list.
    You can use the WORD_LIST defined above, or create your own.
    """
    # TODO: Return your word list
    return [
        "crane", "apple", "hello", "world", "python",
        "house", "water", "light", "music", "dream"
    ]


def test_word_list_fixture(common_word_list):
    """
    Test function demonstrating fixture usage.

    TODO: Students should implement this test to demonstrate using the fixture.
    Test that the fixture works and use it with one of the Wordle functions.
    """
    # TODO: Implement your test using the common_word_list fixture
    examples = [
        # Valid words (case in-sensitive)
        ("crane", True),
        ("apple", True),
        ("HELLO", True),
        ("World", True),
        # Invalid words (not in list)
        ("orange", False),
        ("tree", False),
        # Edge cases (empty string, empty word list)
        ("", False)
    ]

    # TODO: Implement your test cases here
    for word, expected in examples:
        result = is_valid_word(word, common_word_list)
        assert result == expected, f"Expected {expected}, got {result}"