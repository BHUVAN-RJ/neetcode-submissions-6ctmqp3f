'''
position = [4,1,0,7], speed = [2,2,1,1] - Target 10

10 - 4 / 2 || 10 - 1 / 2 || 10 - 0 / 1 || 10 - 7 / 1

3 || 5 || 10 || 3

[[4,2], [1,2], [0,1], [7,1]]

[[7,1], [4,2], [1,2], [0,1]]

[
[0, 10]
[1, 5]
[7, 3] -> if less than 3 doesnt matter
]
use ceil()
all positions are unique

first sort the positions to get the positioning - but you cannot do only that



position=[8,3,7,4,6,5]
speed=[4,4,4,4,4,4]

positions_sorted = [8, 7, 6, 5, 4, 3]

'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(key=lambda x : x[0])

        for car in reversed(cars):
            reach = (target - car[0]) / car[1]
            if not stack:
                stack.append(reach)
            
            elif stack[-1] < reach:
                stack.append(reach)
        
        return len(stack)
        

        