class Solution:
    def isValid(self, s: str) -> bool:
        # while open keep putting into stack
        # we can do this by just checking if val is open
        # the second we reach a closed val, check if top
        # of stack matches closed and keep popping. 
        # if stack empty, return true, else false 

        myStack = []
        closeDic = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in closeDic:
                if myStack and myStack[-1] == closeDic[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(i)
            
        return True if not myStack else False


