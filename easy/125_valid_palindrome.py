class Solution(object):
    import string
    def isPalindrome(self, s):
        s = s.lower()
        sf = ""
        for i in s:
            if i in list(string.ascii_letters) or i in list(string.hexdigits):
                sf += i

        sb = ""
        for j in range(1, len(sf) + 1):
            sb += sf[-j]
        
        return sf == sb