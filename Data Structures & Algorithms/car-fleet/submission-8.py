'''
stack = [](O(n))

position = [4,1,0,7], speed = [2,2,1,1]

cars = [(4,2), (1,2), (0,1), (7,1)](O(n))

sort based on position - 
[(0,1), (1,2), (4,2), (7,1)]
1 - 10-7 = 3/1 = 3
2 - 10-4 = 6/2 = 3 (<= stack top)
3 - 10-2 = 8/2 = 4 (> stack top) - add
4 - 10-0 = 10/1 = 10 (> stack top) - add
[3, 4, 10]
return res

solution - O(n) space  |||| O(n) time

|||||| one more way ||||||



'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(key=lambda x: x[0])

        for car in reversed(cars):
            cur = (target - car[0]) / car[1]
            if not stack:
                stack.append(cur)
            elif stack[-1] < cur:
                stack.append(cur)
        
        return len(stack)
                

        