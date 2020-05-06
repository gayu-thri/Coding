class Solution
{
    public int firstUniqChar(String s) 
    {
        Map<Character, Integer> freq = new HashMap<>();
        
        for(int i=0; i<s.length(); i++)
        { 
            char c = s.charAt(i);
            if(freq.containsKey(c))
                freq.put(c, -1);
            else
                freq.put(c, i);
            //System.out.println(c);
            //System.out.println(freq.get(c));
        }
        int min = Integer.MAX_VALUE;
        for(char ch: freq.keySet())
        {
            if(freq.get(ch) > -1 && freq.get(ch) < min)
                min = freq.get(ch);
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}