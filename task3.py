class NNClassifier:
    name=[]
    gist=[]
    k=0
    gistcount=[]
    def __init__(self):
        f = open('test.txt', 'r')
        lines = f.readlines()
        for line in lines:
            ls=line.split(' ')
            ls = [line.rstrip() for line in ls]
            self.name.append(ls[0])
            ls.pop(0)
            for i in self.gist:
                if (ls==i):
                    gistcount[i]+=1;
            self.gist.append(ls)
            self.k+=1
        print(self.gist)
        f.close()
    def whatIsIt(self, list):
        min=9999999
        h=0
        namenew=""
        for i in range(len(self.gist)):
            r = histDistanve(self.gist[i], list)
            if (r < min):
                min = r
                namenew = self.name[i]
                h=i
            elif (r==min):
                if (self.gistcount[i] > self.gistcount[h]):
                    namenew = self.name[i]
            if min==-1:
                newname=error

        return namenew



def histDistanve(hist1, hist2)->float:
    s=0
    f=0
    if len(hist1)<len(hist2):
        return -1
    while len(hist1) != len(hist2):
        hist1.append(0)
    for i in range(len(hist2)):
        if (hist1[i]==''):
            hist1[i]=0
        s+= (int(hist1[i])-int(hist2[i]))**2
    return s ** 0.5


d=[1,2,4]
a=NNClassifier()
print(a.whatIsIt(d))