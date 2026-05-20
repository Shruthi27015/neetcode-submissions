class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={
        ')':'(',
        '}':'{',
        ']':'['
       } 
        for i in s:
            if i in hm.values():
                stack.append(i)
            else:
                if not stack or stack[-1]!=hm[i]:
                    return False
                stack.pop()
        return len(stack)==0