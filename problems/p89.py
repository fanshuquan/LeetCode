# coding=utf-8
class Solution(object):
    def grayCode(self, n):
        """
        reversed函数好用，区却与list.reverse()
        list.expend()连接一段list，区别于list.append()
        list+=list比list.expend()效率低36ms和24ms的区别，还是挺大区别的
        :type n: int
        :rtype: List[int]
        """
        r = [0]
        for i in range(n):
            tmp = []
            for j in reversed(r):
                tmp.append(j ^ (1 << i))
            r.extend(tmp)
            # r+=tmp
        return r

    def grayCode3(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in range(2 ** n)]

    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        first = [0]
        last = [i for i in range(1, 2 ** n)]
        self.cal(first, last)
        return first

    def is2n(self, x):
        r = 0
        while x != 0:
            if x & 1 == 1:
                r += 1
            x = x >> 1
        return True if r == 1 else False

    def cal(self, first, last):
        if len(last) == 0:
            return True
        for l in last:
            if self.is2n(first[len(first) - 1] ^ l):
                first.append(l)
                last.remove(l)
                if self.cal(first, last):
                    return True
                first.pop()
                last.insert(1, l)
        return False


print Solution().grayCode(2)
# print Solution().is2n(3)
# print [1,2,3][-1:0:-1]
