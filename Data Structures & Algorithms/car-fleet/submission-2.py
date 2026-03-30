class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        
        combined.sort(key=lambda x:x[0])

        stack = []
        print(combined)
        for i in range(len(combined) - 1, -1, -1):
            print(stack, i)
            curCar = combined[i]
            curTime = (target - curCar[0]) / curCar[1]
            print("CURTIME:", curTime)
            if len(stack) and curTime <= stack[-1]:
                continue
            else:
                stack.append(curTime)
        print(stack)
        return len(stack)