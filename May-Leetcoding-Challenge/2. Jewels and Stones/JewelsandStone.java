class Solution {
    public int numJewelsInStones(String J, String S) 
    {
        int count = 0;
        Set setj = new HashSet();   //Ke
        for(char j: J.toCharArray())
            setj.add(j);
        for(char s: S.toCharArray())
            if(setj.contains(s))
                count += 1;
        return count;
    }
}