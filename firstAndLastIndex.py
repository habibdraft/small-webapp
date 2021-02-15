class Solution:
    def searchRange(self, nums, target):
        start = -1
        end = -1
        for index in range(len(nums)):
            if nums[index] == target and start == -1:
                start = index
            if nums[index] != target and start != -1:
                end = index - 1
                break
        if end == -1 and start != -1:
            end = len(nums) - 1
        return [start, end]
