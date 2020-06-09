class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        i = 0
        exist = 0
        for letter in t:
            if i < len(s):
                if s[i] == letter:
                    exist += 1
                    i = i + 1
                else:
                    continue
            else:
                break
        if len(s) == exist:
            return True
        return False