

def triangle(a):
    i=a
    while i>0:
        for j in range(1, i, 1):
            print(' ',end='')
        for j in range(1,2*(a-i+1)):
            print("*",end='')
        print()
        i-=1

def histDistanve(hist1, hist2)->float:
    s=0
    if len(hist1) != len(hist2):
        return -1
    for i in range(len(hist1)):
        s+= (hist1[i]-hist2[i])**2
    return s ** 0.5




triangle(5)
a=[6,9,3]
b=[1,2,3]
print(histDistanve(a, b))

f=open('test.txt','w')
for i in a:
    f.write(str(i))
    f.write(' ')
for i in b:
    f.write(str(i))
    f.write(' ')
f.close()

f=open('test.txt','r')
print(f.readline())
print(f.readline())
f.close()
