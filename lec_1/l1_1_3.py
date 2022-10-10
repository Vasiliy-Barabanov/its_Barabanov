import time
import random

def initListWithRandomNumbers():
    rand_list=[]
    n = 1000
    for i in range(n):
        rand_list.append(random.randint(0,999))
    return rand_list

def calcSumm(arr):
    summ = 0
    for val in arr:
        summ = summ + val
    return summ


a = initListWithRandomNumbers()
# starting time
mini=999999999
maxi=0
counter=0
for i in range(100):
    start = time.time()
    calcSumm(a)
    # end time
    end = time.time()
    # total time taken
    print("Runtime of the calcSumm is ", (end - start),"\n")
    if (end - start) > maxi:
        maxi=(end - start)
    if (end - start) < mini:
        mini=(end - start)
    counter+=(end - start)
print("minimum time is: ", mini,"\n")
print("maximum time is: ", maxi,"\n")
print("middle time is: ", counter/100,"\n")