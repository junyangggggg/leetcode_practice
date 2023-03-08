class Solution(object):
    def findTheDifference(self, s, t):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        dic2 = {}

        for j in t:
            if j not in dic:
                return j 
            elif j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
            
        for k in dic2:
            if dic2[k] != dic[k]:
                return k
