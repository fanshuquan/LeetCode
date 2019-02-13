class Solution(object):
    def nature(self):
        x = 1
        while True:
            yield x, x * (x + 1) // 2
            x += 1

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = self.nature()
        x1, y1 = next(m)
        while True:
            x2, y2 = next(m)
            if n >= y1 and n < y2:
                return x1
            x1, y1 = x2, y2


print Solution().arrangeCoins(3)
# sn = Solution().nature()
# print next(sn)
# print next(sn)
