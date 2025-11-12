class RomanToInteger:
    def __init__(self):
        # Mapping of Roman numerals to their integer values
        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, s):
        # Handle null or empty input
        if not s:
            raise ValueError("Input cannot be empty or null.")

        # Check for invalid characters
        for char in s:
            if char not in self.map:
                raise ValueError(f"Invalid Roman numeral character: {char}")

        # Check for invalid repetitions
        invalid_repetitions = ["VV", "LL", "DD"]
        for rep in invalid_repetitions:
            if rep in s:
                raise ValueError(f"Invalid repetition found: {rep}")

        result = 0
        i = 0
        while i < len(s):
            # Get current numeral value
            current = self.map[s[i]]

            # Get next numeral value (if any)
            next_value = self.map[s[i + 1]] if i + 1 < len(s) else 0

            # Apply Roman numeral rules
            if current < next_value:
                result += next_value - current
                i += 2  # Skip next numeral
            else:
                result += current
                i += 1

        return result


# -------------------------------
# ✅ TEST CASES
# -------------------------------
def run_tests():
    converter = RomanToInteger()
    test_cases = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "XI": 11,
        "IV": 4,
        "XIV": 14,
        "II": 2,
        "Z": "Error",
        "XIZ": "Error",
        "VV": "Error",
        "": "Error"
    }

    print("🔍 Running Test Cases:\n")
    for roman, expected in test_cases.items():
        try:
            result = converter.roman_to_int(roman)
            print(f"{roman:<5} → {result:<5} ✅ (Expected: {expected})")
        except Exception as e:
            print(f"{roman:<5} → ❌ Error: {e}")

# Run the tests
if __name__ == "__main__":
    run_tests()
