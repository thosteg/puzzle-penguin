# From the internet:
# Which digits ABCD so that ABCD * 4 = DCBA?
#
# I did not watch the solution, but here goes:
#
# Digits mean A B C D are in the range [0..9]
# Assuming A B C D are four distinct digits, no two of them denote the same digit.
#
# Otherwise A = B = C = D = 0 would be the obvious (trivial) solution.
#
# It is easier though to just test all combinations.

import copy
import pytest
from typing import List

def get_digits(num: int):
    digits = []
    while num != 0:
        digit = num % 10
        num = num // 10
        digits.insert(0, digit)
    return digits

def test_get_digits():
    assert get_digits(4321) == [4,3,2,1]

def matches_prerequisite(num: int) -> bool:
    """ Not testing if the condition is correct, but if the number matches the outward requirement """
    if isinstance(num, int) == False:
        return False
    
    if num < 0 or num > 9999:
        return False

    digits = set(get_digits(num))
    if len(digits) < 4:
        return False

    return True

def test_matches_prerequisite():
    assert matches_prerequisite(1.234) == False  # No Integer number
    assert matches_prerequisite(-1) == False     # Too small
    assert matches_prerequisite(12345) == False  # Too many digits
    assert matches_prerequisite(1123) == False   # Double digit
    assert matches_prerequisite(1234) == True    # Could be correct (is not)

def digits_to_num(digits: List[int]):
    res = 0
    multiplier = 1
    for digit in reversed(digits):
        res += digit * multiplier
        multiplier *= 10
    return res


def test_digits_to_num():
    assert digits_to_num([1,2,3,4]) == 1234

def reversed_num(num: int):
    return digits_to_num(list(reversed(get_digits(num))))

def test_reversed_num():
    assert reversed_num(1234) == 4321

def check_condition(num: int):
    return matches_prerequisite(num) and num * 4 == reversed_num(num)

def find_numbers():
    """Find numbers that match the condition: ABCD * 4 = DCBA"""
    return [i for i in range(1,10000) if check_condition(i)]

def test_find_number():
    numbers = find_numbers()
    assert len(numbers) > 0
    for num in numbers:
        assert check_condition(num)

if __name__ == "__main__":
    for num in find_numbers():
        print(num)
