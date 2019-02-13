class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(l) for l in list(str(int(''.join([str(d) for d in digits]))+1))]


print Solution().plusOne([1,2,3])
print 0%9