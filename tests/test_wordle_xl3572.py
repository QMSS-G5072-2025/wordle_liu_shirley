from wordle_xl3572.wordle_xl3572 import validate_guess, check_guess
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


