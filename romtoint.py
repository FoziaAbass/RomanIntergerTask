import re

# ---------------------------
# ROMAN → INTEGER CONVERTER
# ---------------------------

def roman_to_int(roman_str):
    if not roman_str or roman_str.strip() == "":
        return "Error: Input is empty"

    roman_str = roman_str.strip().upper()

    roman_vals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    subtractive_rules = {
        'I': ('V', 'X'),
        'X': ('L', 'C'),
        'C': ('D', 'M')
    }

    # Validate characters
    for ch in roman_str:
        if ch not in roman_vals:
            return f"Error: Invalid character '{ch}'"

    # Illegal repetitions
    if re.search(r"(I{4}|X{4}|C{4}|M{4})", roman_str):
        return "Error: Invalid repetition of a numeral more than 3 times"

    if any(bad in roman_str for bad in ("VV", "LL", "DD")):
        return "Error: Invalid repetition of 'V', 'L', or 'D'"

    total = 0
    idx = 0

    while idx < len(roman_str):
        curr_val = roman_vals[roman_str[idx]]

        if idx + 1 < len(roman_str):
            next_val = roman_vals[roman_str[idx + 1]]

            # Subtractive case
            if curr_val < next_val:
                if roman_str[idx] not in subtractive_rules or roman_str[idx + 1] not in subtractive_rules[roman_str[idx]]:
                    return f"Error: Invalid subtractive pair '{roman_str[idx]}{roman_str[idx + 1]}'"

                total += next_val - curr_val
                idx += 2
                continue

        total += curr_val
        idx += 1

    return total


# ---------------------------
# INTEGER → ROMAN CONVERTER
# ---------------------------

def int_to_roman(number):
    if not isinstance(number, int) or number < 1 or number > 3999:
        return "Error: Enter an integer between 1 and 3999"

    numeral_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    remaining = number

    for value, symbol in numeral_map:
        while remaining >= value:
            result.append(symbol)
            remaining -= value

    return "".join(result)


# ---------------------------
# AUTOMATED TESTS
# ---------------------------

# Roman → Int Tests
assert roman_to_int("I") == 1
assert roman_to_int("V") == 5
assert roman_to_int("X") == 10
assert roman_to_int("L") == 50
assert roman_to_int("C") == 100
assert roman_to_int("D") == 500
assert roman_to_int("M") == 1000

assert roman_to_int("XI") == 11
assert roman_to_int("IV") == 4
assert roman_to_int("XIV") == 14
assert roman_to_int("II") == 2

assert roman_to_int("Z") == "Error: Invalid character 'Z'"
assert roman_to_int("XIZ") == "Error: Invalid character 'Z'"
assert roman_to_int("VV") == "Error: Invalid repetition of 'V', 'L', or 'D'"
assert roman_to_int("") == "Error: Input is empty"
assert roman_to_int("IIII") == "Error: Invalid repetition of a numeral more than 3 times"

# Int → Roman Tests
assert int_to_roman(1) == "I"
assert int_to_roman(4) == "IV"
assert int_to_roman(9) == "IX"
assert int_to_roman(14) == "XIV"
assert int_to_roman(44) == "XLIV"
assert int_to_roman(3999) == "MMMCMXCIX"

assert int_to_roman(0) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman(4000) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman(-5) == "Error: Enter an integer between 1 and 3999"
assert int_to_roman("X") == "Error: Enter an integer between 1 and 3999"

print("All automated test cases passed! 🎉\n")


# ---------------------------
# USER INPUT HELPERS
# ---------------------------

def confirm(message):
    """Simple yes/no validator."""
    while True:
        choice = input(message + " (y/n): ").lower().strip()
        if choice in ("y", "n"):
            return choice
        print("Please enter 'y' or 'n'.")


# ---------------------------
# INTERACTIVE PROGRAM
# ---------------------------

if __name__ == "__main__":
    print("🧮 Roman ↔ Integer Converter")
    print("Choose mode once. Type 'exit' anytime.\n")

    mode = input("Choose conversion (1 = Roman→Int, 2 = Int→Roman): ").strip()

    if mode.lower() == "exit":
        if confirm("Do you really want to exit?") == "y":
            print("Goodbye!")
            exit()

    while True:
        if mode == "1":
            user = input("\nEnter a Roman numeral: ").upper().strip()

            if user.lower() == "exit":
                if confirm("Exit the program?") == "y":
                    if confirm("Switch to Integer → Roman?") == "y":
                        mode = "2"
                        continue
                    print("Goodbye!")
                    break
                continue

            print(f"Result: {roman_to_int(user)}")

        elif mode == "2":
            user = input("\nEnter an integer (1–3999): ").strip()

            if user.lower() == "exit":
                if confirm("Exit the program?") == "y":
                    if confirm("Switch to Roman → Integer?") == "y":
                        mode = "1"
                        continue
                    print("Goodbye!")
                    break
                continue

            if not user.isdigit():
                print("Error: Please enter a valid integer")
                continue

            print(f"Result: {int_to_roman(int(user))}")

        else:
            print("Invalid mode. Restart and pick 1 or 2.")
            break
