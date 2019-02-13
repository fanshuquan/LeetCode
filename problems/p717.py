class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        cur = 0
        while cur < len(bits):
            if cur == len(bits) - 1 and bits[cur] == 0:
                return True
            if bits[cur] == 0:
                cur = cur + 1
            if bits[cur] == 1:
                cur = cur + 2
        return False


print Solution().isOneBitCharacter([1, 0, 0])
print Solution().isOneBitCharacter([1, 1, 1, 0])
