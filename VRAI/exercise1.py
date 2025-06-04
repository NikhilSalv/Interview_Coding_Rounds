def is_palindrome(s: str) -> bool:
    """
    The task was to check which test cases are failing and fix the code.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize two pointers
    left, right = 0, len(cleaned) - 1
    
    # Use a while loop to compare characters
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage
if __name__ == "__main__":
    test_string = "A man, a plan, a canal, Panama"
    print(f"Is the string '{test_string}' a palindrome? {is_palindrome(test_string)}")