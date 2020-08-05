"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(root==None):
            return None
        parent,childhead,child = root,None,None
        temp = root
        while(parent):
            while(parent):
                if(parent.left):
                    if(childhead==None):
                        childhead = parent.left
                        child = parent.left
                    else:
                        child.next = parent.left
                        child = child.next
                        
                if(parent.right):
                    if(childhead==None):
                        childhead = parent.right
                        child = parent.right
                    else:
                        child.next = parent.right
                        child = child.next
                        
                parent = parent.next
            parent =  childhead
            childhead,child = None,None
            
        return temp