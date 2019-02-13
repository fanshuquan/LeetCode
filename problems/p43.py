class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval((str(num1)+'*'+str(num2))))


print Solution().multiply('123','456')