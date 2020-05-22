class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = Counter(s1)
        s2dict = Counter()
        ns1, ns2 = len(s1), len(s2)
        if ns1 > ns2:
            return False
        #print(s1dict)
        for i in range(ns2):
            s2dict[s2[i]] += 1
            if i >= ns1:
                if s2dict[s2[i-ns1]] == 1:
                    del s2dict[s2[i-ns1]]
                else:
                    s2dict[s2[i-ns1]] -= 1
            #print(s2dict)
            if s2dict == s1dict:
                return True
        return False
        