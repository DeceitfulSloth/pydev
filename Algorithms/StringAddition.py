class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        runningSum = "0"

        num2 = num2[::-1]
        
        for x in range(len(num2)):
            section = self.simpleMult(num1, num2[x])
            section += x*"0"
            runningSum = self.stringSum(runningSum, section)
            
        return runningSum
    
    def stringSum(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        if len(num1) >= len(num2):
            num2 += (len(num1)-len(num2))*"0"
        else:
            num1 += (len(num2)-len(num1))*"0"
            
        result = ""
        carry = 0
        for x in range(len(num1)):
            res = carry + int(num1[x]) + int(num2[x])
            if res >= 10:
                carry = 1
                res -= 10
            else:
                carry = 0
            result += str(res)
            
        if carry == 1:
            result += "1"
            
        return result[::-1]
    
    def simpleMult(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        num1 = num1[::-1]
        
        carry = "0"
        result = ""
        
        for x in num1:
            s = str(int(x) * int(num2) + int(carry))
            if len(s) == 2:
                carry = s[0]
                s = s[1]
            else:
                carry = "0"
            result += s
        if carry != "0":
            result += carry
            
        return result[::-1]
