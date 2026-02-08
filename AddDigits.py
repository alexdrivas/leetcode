class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum_val = 0
            while num > 0: 
                sum_val += num % 10 # get last digit 
                num //= 10 # remove last digit
            num = sum_val 
        return num