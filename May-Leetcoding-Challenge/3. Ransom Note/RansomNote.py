class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set = set(ransomNote)
        #randomNote = "aaab" -> ransom_set = "ab". Now it contains all elements with count 1.
        
        for char in ransom_set:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
    
        '''
        l = list(magazine)
        for char in ransomNote:
            if char in l:
                l.remove(char)
            else:
                return False
        return True
        ''''