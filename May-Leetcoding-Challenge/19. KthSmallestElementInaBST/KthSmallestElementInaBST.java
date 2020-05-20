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
    public int kthSmallest(TreeNode root, int k) 
    {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        
        b = inorder(root, a);
        return b.get(k-1);
    }
    public List<Integer> inorder(TreeNode root, List<Integer> a)
        {
            if(root == null)
                return a;
            inorder(root.left, a);
            a.add(root.val);
            inorder(root.right,a);
            return a;
        }
}