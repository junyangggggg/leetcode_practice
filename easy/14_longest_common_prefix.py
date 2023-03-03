class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        comm_pref, comm_pref_var = "", ""
        max_len = 0
        for ele in strs:
            if max_len == 0:
                max_len = len(ele)
            elif len(ele) < max_len:
                max_len = len(ele)

        for i in range(max_len):
            for ele in strs:
                if ele == "":
                    return comm_pref
                if comm_pref_var == "":
                    comm_pref_var = ele[i]
                elif comm_pref_var != ele[i]:
                    return comm_pref
                else:
                    pass
            comm_pref += comm_pref_var
            comm_pref_var = ""
        return comm_pref