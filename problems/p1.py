class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for k,v in enumerate(nums):
            x = target-v
            if x in map:
                return [map[target-v],k]
            map[v]=k





print(Solution().twoSum([2, 7, 11, 15], 9))
