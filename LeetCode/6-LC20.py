class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        opn=["{","[","("]
        close=["}","]",")"]
        for i in range(len(s)):
            if s[i] in opn:
                stack.append(s[i])
                #top=top+1
            if s[i] in close:
                if not stack:
                    return False

                match s[i]:
                    case "}":
                        if stack[-1]=="{":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if stack[-1]=="[":
                            stack.pop()
                        else:
                            return False
                    case ")":
                        if stack[-1]=="(":
                            stack.pop()
                        else:
                            return False
        return len(stack)==0