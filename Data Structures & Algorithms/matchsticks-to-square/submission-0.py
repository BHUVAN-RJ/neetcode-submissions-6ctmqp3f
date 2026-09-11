'''
- i have matchsticks with certain lenghts
- have to make squares
- I can add up smaller ones to make bigger length but cannot break smaller
- return true if we can form square else false


- if we use few sticks and form square - false

question:
- must use all sticks ? - true


[1,4,2,2,4,3]


[4,4]


logic:
- since cannnot break - longest should be one of the side


thining:
- scan the entire thing - find max
- will have a count sides = 4( decrement accourdingly)
- find all elements that sum up to that 



'''



class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    
                    sides[j] -= matchsticks[i]
                
            return False
        
        return backtrack(0)



        


        
                




        