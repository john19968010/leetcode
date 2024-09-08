class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        formula is f(a, b) + b >= a
        if a == b and a+1 == b-1 ..... is parlindrome
           a+1 != b-1 -> not parlindrome
        """
        len_s = len(s)
        ans = 0
        # Record from index to index is parlindrome or not
        records = [[False] * len_s for _ in range(len_s)]

        for i in range(len_s):
            records[i][i] = True
            ans += 1

        for i in range(len_s - 1):
            if s[i] == s[i + 1]:
                records[i][i + 1] = True
                ans += 1

        cal_str_len = 3

        while cal_str_len <= len_s:
            for i in range(len_s - cal_str_len + 1):
                s_i, e_i = i, i + cal_str_len - 1
                if s[s_i] == s[e_i] and records[s_i + 1][e_i - 1]:
                    records[s_i][e_i] = True
                    ans += 1
            cal_str_len += 1

        return ans
