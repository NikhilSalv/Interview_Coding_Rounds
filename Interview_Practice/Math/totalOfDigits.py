"""
Given an integer → sum its digits → if the result has more than one digit → repeat until you get a single-digit result.
"""
def totalOfDigits(n):
    
    while n > 9:
        total = 0
        while n:
            total += n % 10
            n //= 10
        n = total
    return total


if __name__ == "__main__":
    print(totalOfDigits(687))