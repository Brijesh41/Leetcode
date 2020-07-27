class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        self.inorder(root,0,sum,prefix)
        return self.count
    def inorder(self,root,currsum,target,prefix):
        if(root):
            currsum+=root.val
            self.count+=prefix[currsum-target]
            prefix[currsum]+=1
            self.inorder(root.left,currsum,target,prefix)
            self.inorder(root.right,currsum,target,prefix)
            prefix[currsum]-=1
            
        
        