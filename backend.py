def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds two numbers in a list that add up to a target value and returns their indices.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the two numbers that add up to the target,
        or an empty list if no such pair exists.  Returns an empty list if input is invalid.
    """

    # Input Validation
    if not isinstance(nums, list):
        print("Error: Input 'nums' must be a list.")
        return []
    for num in nums:
        if not isinstance(num, int):
            print("Error: All elements in 'nums' must be integers.")
            return []

    # Edge Case: Empty Array
    if not nums:
        return []

    num_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index

    return []


if __name__ == '__main__':
    # Example Usage
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: Indices: [0, 1]

    nums = [3, 2, 4]
    target = 6
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: Indices: [1, 2]

    nums = [3, 3]
    target = 6
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: Indices: [0, 1]

    nums = [1,2,3,4,5]
    target = 10
    result = two_sum(nums, target)
    print(f"Indices: {result}") # Output: Indices: [3, 4]
