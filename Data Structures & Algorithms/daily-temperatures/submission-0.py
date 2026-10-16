class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    index = stack.pop()[1]
                    output[index] = i - index
                stack.append((temperatures[i], i))
                
        return output