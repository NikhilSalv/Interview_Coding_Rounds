def find_first_duplicate(nums):
    """
    The task was to find the error in the code and fix it.
    The code was returning -1 even if num is in seen. 
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

# Example usage
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 2, 5, 6]
    print(f"The first duplicate is: {find_first_duplicate(test_list)}")  # Output: 2

    test_list_no_duplicates = [1, 2, 3, 4, 5]
    print(f"The first duplicate is: {find_first_duplicate(test_list_no_duplicates)}")  # Output: -1