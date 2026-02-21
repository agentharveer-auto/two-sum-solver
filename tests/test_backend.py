import pytest
from backend import two_sum


def test_two_sum_valid_input():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3, 4, 5], 100) == []

def test_two_sum_duplicate_numbers():
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_negative_numbers():
    assert two_sum([-1, -3, 5, 7], 4) == [0, 2]

def test_two_sum_empty_array():
    assert two_sum([], 5) == []

def test_two_sum_invalid_input_nums_not_list():
    assert two_sum("1,2,3", 5) == []

def test_two_sum_invalid_input_nums_not_int():
    assert two_sum([1, "a", 3], 5) == []

def test_two_sum_large_array():
    nums = list(range(1000))
    target = 1999
    assert two_sum(nums, target) == [999, 1000-1]


def test_two_sum_zero_target():
    assert two_sum([-1, 1], 0) == [0, 1]

def test_two_sum_zero_in_array():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
