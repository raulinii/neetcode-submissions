class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       stack = []
       output = 0
       sPositions = [(p, s) for p, s in zip(position, speed)]
       sPositions.sort(reverse=True)

       for p, s in sPositions:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
       return len(stack)