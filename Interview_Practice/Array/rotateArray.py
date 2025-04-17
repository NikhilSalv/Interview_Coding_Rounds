class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None  Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print("len", n)
        if n == 0:
            return

        k %= n
        count = 0          # how many elements we've moved so far
        start = 0          # starting index for each cycle

        while count < n:
            current = start
            prev_value = nums[start]
            # perform one cycle
            while True:
                next_idx = (current + k) % n
                # swap(prev_value) into nums[next_idx], and grab displaced value
                nums[next_idx], prev_value = prev_value, nums[next_idx]
                current = next_idx
                count += 1
                # if we’ve come full‑circle, break out of this cycle
                if current == start:
                    break

            start += 1    # move to the next start position for a new cycle


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]  # Expected output [5,6,1,2,3,4]
    result = Solution()
    print(result.rotate(nums, 2))
    print("final output ", nums)