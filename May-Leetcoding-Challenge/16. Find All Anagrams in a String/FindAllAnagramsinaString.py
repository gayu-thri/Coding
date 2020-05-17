class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        
        ns, np = len(s), len(p)
        
        result = []
        pdict = Counter(p)
        sdict = Counter()
                
        for i in range(ns):
            sdict[s[i]] += 1
            if(i >= np):
                if sdict[s[i-np]] == 1:
                    del sdict[s[i-np]]
                else:
                    sdict[s[i-np]] -= 1
            #print(sdict)  
            if sdict == pdict:
                result.append(i-np+1)
        
        return result
        

        