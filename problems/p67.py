class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        inta = int(a, base=2)
        intb = int(b, base=2)
        return str(bin(inta+intb))[2:]

    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)
        next = 0
        sum = 0
        rlist = []
        while lena > 0 or lenb > 0:
            aa = 0
            bb = 0
            if lena > 0:
                aa = int(a[lena - 1])
            if lenb > 0:
                bb = int(b[lenb - 1])
            tmp = next + aa + bb
            if tmp == 0:
                next = 0
                sum = 0
            if tmp == 1:
                next = 0
                sum = 1
            if tmp == 2:
                next = 1
                sum = 0
            if tmp == 3:
                next = 1
                sum = 1
            rlist.append(str(sum))
            lena -= 1
            lenb -= 1
        if next == 1:
            rlist.append('1')
        rlist.reverse()
        return ''.join(rlist)


print Solution().addBinary('1010', '1011')
print str(bin(2))[2:]
