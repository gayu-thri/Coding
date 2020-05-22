class Solution {
    public List<Integer> findAnagrams(String s, String p) 
    {
        Map<Character, Integer> sdict = new HashMap<>();
        Map<Character, Integer> pdict = new HashMap<>();
        List<Integer> result = new ArrayList<>();
        int ns = s.length();
        int np = p.length();
        if(ns == 0 || s == null || np == 0 || p == null || ns<np)
            return result;
        for(char c: p.toCharArray())
        {
            if(pdict.containsKey(c))
                pdict.put(c, pdict.get(c) + 1);
            else
                pdict.put(c, 1);
        }
        //System.out.println(pdict);
        for(int i=0; i<ns; i++)
        {
            if(sdict.containsKey(s.charAt(i)))
                sdict.put(s.charAt(i), sdict.get(s.charAt(i)) + 1);
            else
                sdict.put(s.charAt(i), 1);
            if(i >= np)
            {
                if(sdict.get(s.charAt(i-np)) == 1)
                    sdict.remove(s.charAt(i-np));
                else
                    sdict.put(s.charAt(i-np), sdict.get(s.charAt(i-np)) - 1);
            }
            //System.out.println(sdict);
            if(sdict.equals(pdict))
                result.add(i-np+1);
        }
        return result;
    }
}