# goal is to create a key value store that also have time associated with each value
# set -> key, value, time
# get -> return value for key, with value timestamp <= get timestamp
# get -> if multiple values -> largest prev time stamp -> closest to the get_timestamp 
# if no value return ''
# cases -> for a key, one value, no value(key has other values with timestamp < get_timestamp  
# and key doesnt have values < get_timestamp), multiple value
# QUESTION: what to do if there is already a value but diff time -> update time for the val
# what to do if there is already a value with same time -> update and it does nothin
# ex - 1
# SET: k: alice || v = happy || time: 1
# GET: (alice, 1) -> alice has value that has time = 1 -> return it
# GET: (alice, 2) -> alice doesnt have time = 2, but has time = 1 <= 2 ->return time = 1
# SET: k: alice || v = sad || time:2
# GET: (alice, 3) -> doesnt have at time = 3 but has at time = 2 < 3 but 2 > 1 so return sad
# solution assumptions:
# 1. solution is not stored in any order(ascending or decending)
# solution:
#
# {key:value} -> value -> also {} --> {key:{}}
# SET -> if key not present -> add key:{value:time}
# if key present add to the val dict
# GET -> case 1. exact match for get_timestamp -> return that specific value
# case 2. exact match not present -> 
# for key, val, time: if time < get_time: res = curtime if get_time - curtime < gettime - res else res
# res edge case if not present -> ""



class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][value] = timestamp
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        res = ''
        for value,time in self.store[key].items():
            if time <= timestamp:
                if res == '':
                    res = (value, time)
                    continue
                res = (value,time) if timestamp - time <= timestamp - res[1] else res
        
        return res[0] if res != '' else ''
            

# {key1:{val1:10}}








