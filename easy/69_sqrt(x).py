class Solution(object):
    def mySqrt(self, x):
        i = 0
        while i <= x:
            if i**2 <= x:
                i += 1
            else:
                break
        return i - 1