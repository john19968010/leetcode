class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        records = [0 for i in range(len_s)]
        res = len_s

        def check_substring_is_parlindrome(start_i: int) -> int:
            """
            1. find value of the latest index in array is same as the first one.
            2. store the first and latest index as tuple in records
            """
            last_i = records[start_i] or len_s - 1

            for cur_i in range(last_i, start_i, -1):
                temp_fir_i = start_i
                temp_last_i = cur_i
                is_parlindrome = True
                while temp_last_i > temp_fir_i:
                    if s[temp_fir_i] != s[temp_last_i]:
                        is_parlindrome = False
                        break
                    temp_fir_i += 1
                    temp_last_i -= 1

                if is_parlindrome:
                    add_num = (cur_i - start_i) // 2
                    for _ in range(start_i, cur_i):
                        records[_] = cur_i
                    return add_num
            return 0

        for i in range(len_s):
            res += check_substring_is_parlindrome(i)

        return res
