
class Solution:
    def sumOddLengthSubarrays(self, arr):
        sum = 0
        i = 0
        while i < len(arr):
            j = i
            while j < len(arr):
                k = i
                while k <= j:
                    sum += arr[k]
                    k += 1

                j += 2

            i += 1
        return sum
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOddLengthSubarrays([1,4,2,5,3]))  # Example test case
    print(solution.sumOddLengthSubarrays([1,2]))        # Example test case
    print(solution.sumOddLengthSubarrays([10,11,12]))   # Example test case