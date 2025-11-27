from collections import deque

class Solution:
    def solve(self, A):
        q = deque()
        freq = {}
        result = []

        for ch in A:
            # Increase frequency
            freq[ch] = freq.get(ch, 0) + 1

            # Add to queue
            q.append(ch)

            # Remove repeating chars from queue front
            while q and freq[q[0]] > 1:
                q.popleft()

            # Append result
            if not q:
                result.append('#')
            else:
                result.append(q[0])

        return ''.join(result)

if __name__ == "__main__":
    A = "abadbc"
    solution = Solution()
    print(solution.solve(A))  # Output: "aabbdd"