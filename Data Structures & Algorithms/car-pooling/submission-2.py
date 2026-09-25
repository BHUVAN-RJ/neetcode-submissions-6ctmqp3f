'''
capacity of car = 4

num of passenges, from, to
[4,1,2]
[3,2,4]

    p1. d1. p2. d2
0---1---2---3---4---5---


###EX2###
capacity of car = 4

num of passenges, from, to
[2,1,3]
[3,2,4]

    p1  p2 
0---1---2---3---4---5---

cur_car_cap = 2 + 3 > capacity -> fail


heapify - logn
sorting - nlogn

sort i/p and process one by one
using sorting/heap I can get immediate next pick up
how to check where then drop-off
1. the first guy drops off first
2. the second guy / any other guy drops off first
3. all drop off together

another heap - to get immediate next drop off.

1. heap - 1 for immediate next pick up
2. heap - 2 for immediate next drop off
3. immediately return Flase if cant
'''



class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickUpHeap = [[pickup, dropoff, p] for p, pickup, dropoff in trips]
        dropOffHeap = [[dropoff,pickup, p] for p, pickup, dropoff in trips]
        heapq.heapify(pickUpHeap)
        heapq.heapify(dropOffHeap)

        curCap = 0
        dist = 0
        while pickUpHeap :
            # print(dist)
            dist = pickUpHeap[0][0]
            while dropOffHeap and dropOffHeap[0][0] <= dist:
                    dropped = heapq.heappop(dropOffHeap)
                    # print("dropped", dropped, capacity)
                    curCap -= dropped[2]
            
            while pickUpHeap and pickUpHeap[0][0] == dist:
                    picked = heapq.heappop(pickUpHeap)
                    # print("picked", picked, capacity)
                    curCap += picked[2]
                    if curCap > capacity:
                        return False
            
            
        
        return True
                



        







