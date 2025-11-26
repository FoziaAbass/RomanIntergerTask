# Run tests using: pytest -v
import pytest
from romantointerger import roman_to_int, int_to_roman


# -----------------------------
# BASIC ROMAN NUMERAL CHECKS
# -----------------------------

def test_single_symbols():
    expected = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }

    for numeral, value in expected.items():
        assert roman_to_int(numeral) == value


# -----------------------------
# SIMPLE REPETITIONS
# -----------------------------

def test_small_repetitions():
    assert roman_to_int("II") == 2
    assert roman_to_int("XX") == 20


# -----------------------------
# SEQUENTIAL ADDITIVE VALUES
# -----------------------------

def test_additive_sequences():
    assert roman_to_int("VI") == 6
    assert roman_to_int("XV") == 15


# -----------------------------
# SUBTRACTIVE PATTERNS
# -----------------------------

def test_subtractive_cases():
    pairs = {
        "IV": 4,  "IX": 9,
        "XL": 40, "CM": 900,
        "XIV": 14
    }

    for roman, value in pairs.items():
        assert roman_to_int(roman) == value


# -----------------------------
# INVALID INPUT SYMBOLS
# -----------------------------

def test_bad_characters():
    assert roman_to_int("Z") == "Error: Invalid character 'Z'"
    assert roman_to_int("XIZ") == "Error: Invalid character 'Z'"


# -----------------------------
# REPEAT RULE VIOLATIONS
# -----------------------------

def test_invalid_repeats():
    assert roman_to_int("IIII") == "Error: Invalid repetition of a numeral more than 3 times"
    assert roman_to_int("VV") == "Error: Invalid repetition of 'V', 'L', or 'D'"
    assert roman_to_int("") == "Error: Input is empty"


# -----------------------------
# INT → ROMAN CONVERSIONS
# -----------------------------

def test_integer_to_roman_valid():
    examples = {
        1: "I",
        4: "IV",
        9: "IX",
        14: "XIV",
        44: "XLIV",
        3999: "MMMCMXCIX"
    }

    for num, roman in examples.items():
        assert int_to_roman(num) == roman


def test_integer_to_roman_invalid():
    invalid_inputs = [0, 4000, -2, "ABC"]
    for val in invalid_inputs:
        assert int_to_roman(val) == "Error: Enter an integer between 1 and 3999"


# -----------------------------
# OPTIONAL: RUNNING DIRECTLY
# -----------------------------

if __name__ == "__main__":
    result_code = pytest.main(["-v", __file__])
    if result_code == 0:
        print("\n🎉 All tests completed successfully!")
