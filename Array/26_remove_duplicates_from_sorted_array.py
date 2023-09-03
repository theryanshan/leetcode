# Time: O(n)
# Space: O(1)
# elements at the left side of l is the element to keep, if nums[r] != nums[l - 1], then nums[r] is the element to keep
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
