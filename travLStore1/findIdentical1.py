import sys

#print "list of objects: ", sys.argv[1]
#print "list of objects: ", type(sys.argv[1])
#print "put into array objects: ", sys.argv[1].split(',')

m={}
def rmDup():

    # Find duplicates 
    for e1 in a1:
        m[e1]=0
        for e2 in a1:
            if e1 == e2:
                if (m[e1]):
                    m[e1]+=1
                else:
                    m[e1]=1

    # Delete the identical ones
    for k, v in m.iteritems():
        #print k, v
        if v > 1:
            for i in range(0, v-1):
                a1.remove(k)


a1 = sys.argv[1]
#print "sys.argv", a1
if len(sys.argv[1]) >= 1:
    a1 = a1.split(',')
    rmDup()
    print a1
else:
    print a1

# Checks
#print "initial array: ",a1
#rmDup()
#print "final array: ",a1
#print "initial recurrences: ",m
#rmDup()
#print "final recurrences: ",m
