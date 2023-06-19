# https://leetcode.com/problems/top-k-frequent-elements/description/
# Time: O(n)
# Space: O(n)
# One liner: the max frequency is the total count of nums, use an array with frequency as the index

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            frequency[c].append(n)

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
