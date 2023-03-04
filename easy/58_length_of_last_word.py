class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev_str = ""
        for i in range(1, len(s) + 1):
            if s[-i] != " ":
                rev_str += s[-i]
            elif rev_str != "" and s[-i] == " ":
                break
            elif rev_str == "" and s[-i] == " ":
                pass
        
        return len(rev_str)