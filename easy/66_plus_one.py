class Solution(object):
    def plusOne(self, digits):
        lst_of_9 = []
        if digits[-1] == 9:
            for i in range(1, len(digits) + 1):
                if digits[-i] == 9:
                    lst_of_9.append(-i)
                else:
                    break

        if len(lst_of_9) == 0:
            digits[-1] += 1
        else:
            for i in lst_of_9:
                digits[i] = 0
            if len(lst_of_9) == len(digits):
                digits.insert(0, 1)
            else:
                digits[lst_of_9[-1] - 1] += 1
        return digits
