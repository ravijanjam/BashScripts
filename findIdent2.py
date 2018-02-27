
a1 = [1, 2, 3, 2, 2, 7]

print a1[1:len(a1)]
print a1[2:len(a1)]
print a1[3:len(a1)]

for i in range(0, len(a1)):
    print i, a1[i]


def blah1():
    for i in range(0, len(a1)):
        # print a1[i:len(a1)]
        for e in a1[i:len(a1)]:
            print e
            if a1[i] == e:
                print a1[i]
        

a1 = [1, 2, 3, 2, 2, 7]
def blah2():
    for i in range(0, len(a1)):
        # print a1[i:len(a1)]
        cc=0
        for e in a1[i:len(a1)]:
            #print e
            if a1[i] == e:
                cc+=1
    print a1[i], cc
        
#blah2()


a1 = [1, 2, 3, 2, 2, 7, 5, 7]
m={}
def blah2():
    for i in range(0, len(a1)):
        # print a1[i:len(a1)]
        cc=0
        for e in a1[i:len(a1)]:
            #print e
            if a1[i] == e:
                cc+=1
    print a1[i], cc
        
#blah2()

a1 = [1, 2, 3, 2, 2, 7, 5, 7]
m={}
def blah3():
    for e1 in a1:
        m[e1]=0
        for e2 in a1:
            if e1 == e2:
                if (m[e1]):
                    m[e1]+=1
                else:
                    m[e1]=1

blah3()
print a1
print m

#a = [1, 2, 3, 2, 5]
#print a
#a.remove(2)
#a.remove(2)
#print a
