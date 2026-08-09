#Create a function that measures how long a large loop takes to execute using time.time() or time.perf_counter().

#-Importing:
import time

#-Creating function:
def exTime(iterable,wait=0):
    before = time.perf_counter() #Start counting
    for i in iterable:
        time.sleep(wait)
    after = time.perf_counter() #Finish counting
    return after - before

#-Iterable:
myList = [1,2,3,4,5]

#-Result
print(exTime(myList,1))