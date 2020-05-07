/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) 
    {   if(root == null)
        {
            return false;
        }
        Map<Integer, int[]> map = new HashMap<>();  //xinfo & yinfo are implemented using map
        
        dfs(root,x ,y, 0, 0, map);
        return (map.get(x)[0] == map.get(y)[0]) && (map.get(x)[1] != map.get(y)[1]);  //same depth diff. parents
        
    }
    private void dfs(TreeNode root,int x, int y, int depth, int parent, Map<Integer, int[]> map)
    {
        if(root == null)
        { 
            return ;
        }
        if(root.val == x)
        { 
            map.put(x, new int[]{depth, parent}); 
        }
        if(root.val == y)
        {
            map.put(y, new int[]{depth, parent});
        }
        dfs(root.left, x, y, depth + 1, root.val, map);
        dfs(root.right, x, y, depth + 1, root.val, map);
    }
}