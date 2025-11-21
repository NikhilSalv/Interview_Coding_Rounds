
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset = set(jewels)
        count = 0
        for ch in stones:
            if ch in jewelset:
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(sol.numJewelsInStones(jewels, stones))  # Expected output: 3
    jewels = "z"
    stones = "ZZ"
    print(sol.numJewelsInStones(jewels, stones))  # Expected output: 0
