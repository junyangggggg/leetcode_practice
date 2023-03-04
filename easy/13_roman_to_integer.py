class Solution(object):
    def romanToInt(self, s):
        dic = {"I": 1, 
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        
        n = 0
        t = dic[s[0]]

        for i in range(len(s)):
            if t < dic[s[i]]:
                n = n - t + dic[s[i]] - dic[s[i - 1]]
            else:
                n += dic[s[i]]
            t = dic[s[i]]
        return n
