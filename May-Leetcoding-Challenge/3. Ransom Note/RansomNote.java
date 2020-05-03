class Solution {
    public boolean canConstruct(String ransomNote, String magazine) 
    {
        Map<Character, Integer> freq = new HashMap<>();  //Dictionary in Python
        
        for(char m: magazine.toCharArray())     //put() & get() function in HashMap() -> .put(char,freq)
            if(freq.containsKey(m))
                freq.put(m, freq.get(m) + 1);
            else
                freq.put(m,1);
        
        for(char r: ransomNote.toCharArray())
            if(freq.containsKey(r))
                if(freq.get(r) > 1)
                    freq.put(r, freq.get(r) - 1);   //as we check remove it from magazine.
                else
                    freq.remove(r);
            else
                return false;
                
        return true;
    }
}