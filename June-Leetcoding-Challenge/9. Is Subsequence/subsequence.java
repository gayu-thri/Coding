class Solution {
    public boolean isSubsequence(String s, String t) 
    {
        if(s.length() == 0)
            return true;
        
        int i = 0, exist = 0;
        for(char letter: t.toCharArray()){
            if(i < s.length())
            {
                if(s.charAt(i) == letter)
                {
                    exist += 1;
                    i += 1;
                }
                else
                    continue;
            }
            else
                break;
        }
        if(exist == s.length())
            return true;
        return false;
    }
}