class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        lst  = []
        for key, value in dic.items():
            lst.append(value)
        m = max(lst)
        for key, value in dic.items():
            if m == value:
                return key
