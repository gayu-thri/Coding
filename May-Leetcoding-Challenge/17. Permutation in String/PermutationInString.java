class Solution {
    public boolean checkInclusion(String s1, String s2) 
    {
        Map<Character, Integer> s1dict = new HashMap<>();
        Map<Character, Integer> s2dict = new HashMap<>();
        
        int ns1 = s1.length(), ns2 = s2.length();
        if(ns1>ns2)
            return false;
        for(int i=0; i<ns1; i++)
        {
            if(s1dict.containsKey(s1.charAt(i)))
               s1dict.put(s1.charAt(i), s1dict.get(s1.charAt(i)) + 1);
            else
               s1dict.put(s1.charAt(i), 1);
        }
        for(int i=0; i<ns2 ; i++)
        {   if(s2dict.containsKey(s2.charAt(i)))
                s2dict.put(s2.charAt(i), s2dict.get(s2.charAt(i)) + 1);
            else
                s2dict.put(s2.charAt(i), 1);
            if(i >= ns1)
            {
                if(s2dict.get(s2.charAt(i-ns1)) == 1)
                    s2dict.remove(s2.charAt(i-ns1));
                else
                    s2dict.put(s2.charAt(i-ns1), s2dict.get(s2.charAt(i-ns1)) - 1);
            }
            if(s2dict.equals(s1dict))
                return true;
        }
        return false;
    }
}