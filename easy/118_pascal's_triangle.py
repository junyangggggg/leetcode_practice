class Solution(object):
    def generate(self, numRows):
        lst = []
        for i in range(numRows):
            if i == 0:
                sub_lst = [1]
            else:
                for j in range(i):
                    if j == 0:
                        sub_lst = [1]
                    else:
                        k = lst[i - 1][j - 1] + lst[i - 1][j]
                        sub_lst += [k]
                sub_lst += [1]
            lst.append(sub_lst)
        return lst