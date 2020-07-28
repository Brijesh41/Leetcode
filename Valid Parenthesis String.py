class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        
        for j,i in enumerate(s):
            if(i==")"):
                if(len(stack)==0):
                    return False
                else:
                    leftopen = False
                    ans = []
                    while(stack):
                        if(stack[-1]=="("):
                            stack.pop()
                            leftopen = True
                            break
                        else:
                            stack.pop()
                            ans.append("*")
                    if(leftopen==True):
                        stack.extend(ans)
                    else:
                        stack.extend(ans)
                        stack.pop()
            elif(i=="*"):
                stack.append("*")
            else:
                stack.append("(")
        print(stack)
        if(len(stack)==0):
            return True
        newstack = []
        
        for i in stack:
            if(i=="*"):
                if(len(newstack)==0):
                    pass
                else:
                    newstack.pop()
            else:
                newstack.append(i)
        if(len(newstack)==0):
            return True
        return False
    
        