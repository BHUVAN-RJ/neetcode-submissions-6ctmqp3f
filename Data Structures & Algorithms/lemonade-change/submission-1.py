class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}
        for bill in bills:
            change[bill] += 1
            bill -= 5
            while bill != 0:
                if bill >= 10 and change[10] > 0:
                    change[10] -= 1
                    bill -= 10
                elif bill >= 5 and change[5] > 0:
                    change[5] -= 1
                    bill -= 5
                else:
                    return False
            
        return True

        
        