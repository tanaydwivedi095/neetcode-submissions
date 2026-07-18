class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 1
        element = nums[0]
        for num in nums:
            if element == num:
                freq += 1
            else:
                freq -= 1
                if freq <= 0:
                    freq = 1
                    element = num
        return element 