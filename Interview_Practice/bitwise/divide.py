class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle division by zero
        if divisor == 0:
            return INT_MAX
        
        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        quotient = 0

        # Bit manipulation approach
        for i in range(31, -1, -1):
            # Check if (divisor << i) fits into the remaining dividend
            print("i : ", i, dividend_abs, bin(dividend_abs), dividend_abs >> i,bin(dividend_abs >> i),"divisor_abs : ", divisor_abs, bin(divisor_abs))
            if (dividend_abs >> i) >= divisor_abs:
                quotient += 1 << i          # Add 2^i to quotient
                print(quotient, bin(quotient),"Updated quotient : ", quotient, bin(quotient))
                print(bin(divisor_abs), " divisor shifted : ", divisor_abs << i, bin(divisor_abs << i))
                dividend_abs -= divisor_abs << i  # Subtract (divisor * 2^i) from dividend
                print("Updated dividend_abs : ", dividend_abs, bin(dividend_abs))

        # Apply the sign
        if negative:
            quotient = -quotient

        return quotient

if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(10, 3))   # Example test case
    # print(solution.divide(7, -3))   # Example test case
    # print(solution.divide(0, 1))    # Example test case
    # print(solution.divide(1, 1))    # Example test case
    # print(solution.divide(-2147483648, -1))  # Example test case