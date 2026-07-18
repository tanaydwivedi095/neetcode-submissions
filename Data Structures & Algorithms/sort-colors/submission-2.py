class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lPtr = 0
        rPtr = len(nums)-1
        mPtr = 0
        while mPtr <= rPtr:
            if nums[mPtr] == 0:
                nums[lPtr], nums[mPtr] = nums[mPtr], nums[lPtr]
                lPtr+=1
                mPtr+=1
            elif nums[mPtr] == 2:
                nums[rPtr], nums[mPtr] = nums[mPtr], nums[rPtr]
                rPtr-=1
            else:
                mPtr+=1