from random import randint

def calcHist(tdata):
#   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hist = [0]*10
    for i in range(1000000):
        if 0<=tdata[i]<100:
            hist[0]+=1
        if 100 <= tdata[i] < 200:
            hist[1] += 1
        if 200<=tdata[i]<300:
            hist[2]+=1
        if 300 <= tdata[i] < 400:
            hist[3] += 1
        if 400<=tdata[i]<500:
            hist[4]+=1
        if 500 <= tdata[i] < 600:
            hist[5] += 1
        if 600<=tdata[i]<700:
            hist[6]+=1
        if 700 <= tdata[i] < 800:
            hist[7] += 1
        if 800<=tdata[i]<900:
            hist[8]+=1
        if 900 <= tdata[i] < 1000:
            hist[9] += 1
#   Calculate histogram for tdata List
#   hist [0] = number of values in tdata from 0..99
#   hist [1] = number of values in tdata from 100..199
#   hist [2] = number of values in tdata from 200..299
#   ...
#   hist [9] = number of values in tdata from 900..sys.maxint
    return hist
#   data contains List with size 1000 000 with 0 values
data = [0]*1000000
for i in range(1000000):
    data[i]=randint(0,999)
print(data)
a = calcHist(data)
print(a)