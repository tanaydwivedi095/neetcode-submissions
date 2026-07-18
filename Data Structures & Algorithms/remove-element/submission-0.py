class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lPtr = 0
        for rPtr in range(0, len(nums)):
            if nums[rPtr] != val:
                nums[lPtr] = nums[rPtr]
                lPtr+=1
        return lPtr
