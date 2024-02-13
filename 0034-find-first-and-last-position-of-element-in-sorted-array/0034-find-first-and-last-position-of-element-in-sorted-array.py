class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return ([-1,-1])
        x = 0
        for i in range(len(nums)):
            if nums[i] == target:
                x = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                return ([x,i])