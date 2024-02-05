class Solution:
    def sortColors(self, nums: List[int]) -> None:

        sorted_nums = []

        n_max = max(nums)
        n_min = min(nums)
        count_range = n_max - n_min + 1
        count = [0] * count_range

        for i in nums:
            count[i - n_min] += 1

        for j in range(count_range):
            for k in range(count[j]):
                sorted_nums.append(j + n_min)

        for i in range(len(sorted_nums)):
            nums[i] = sorted_nums[i]