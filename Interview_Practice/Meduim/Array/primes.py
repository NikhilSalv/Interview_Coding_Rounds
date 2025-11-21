class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        primes = []
        print("Integer is " , n)
        for i in range(2,n):
            for j in range(2,int(i**0.5) + 1):
               if i % j == 0:
                   break
            else:
                primes.append(i)  
        return primes



if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(10))  # Expected output 4 (primes are 2, 3, 5, 7)
    print(sol.countPrimes(0))   # Expected output 0
    print(sol.countPrimes(1))   # Expected output 0 
    print(sol.countPrimes(12))  # Expected output 8 (primes are 2, 3, 5, 7, 11, 13, 17, 19)