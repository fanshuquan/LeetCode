class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))
        # return str(eval(num1+'+'+num2))
        # return str(eval(num1) + eval(num2))
    def addStrings1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        longer = num1
        shorter = num2
        if len(num1) < len(num2):
            longer = num2
            shorter = num1
        shorter = '0'*(len(longer)-len(shorter))+shorter
        ret = ''
        ext = 0
        for i in reversed(range(len(longer))):
            sum = int(longer[i])+int(shorter[i])+ext
            ext = sum/10
            t = sum%10
            ret+=str(t)
        return ret[::-1] if ext == 0 else (ret + str(ext))[::-1]
        # return ''.join(reversed(ret)) if ext==0 else ''.join(reversed(ret+str(ext)))


print Solution().addStrings('12','134')
print '123'[::-1]
