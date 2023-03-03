class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_pal = ""
        for i in range(1, len(str_x) + 1):
            str_pal += str_x[-i]
        return str_x == str_pal