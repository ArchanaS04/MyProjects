#Data set
#data = [
#        ['Transaction1',['Pen','Pencil','Scale']],
#        ['Transaction2',['Pencil','Calculator']],
#        ['Transaction3',['Pencil','Notebook']],
#        ['Transaction4',['Pen','Pencil','Calculator']],
#       ['Transaction5',['Pen','Notebook']],
#        ['Transaction6',['Pencil','Notebook']],
#       ['Transaction7',['Pen','Notebook']],
#       ['Transaction8',['Pen','Pencil','Notebook','Scale']],
#        ['Transaction9',['Pen','Pencil','Notebook']]
 #]
data=[]
print("Enter total number of transactions:")
n=int(input())
for i in range(n):
    x=input("Enter the transaction ID:")
    l1=[]
    l1.append(x)
    y=int(input("Enter the number of items:"))
    l2=[]
    print("Enter items:")
    for j in range(y):
        l2.append(input())
    l1.append(l2)
    data.append(l1)

print("Transaction Details:\n")
for i in data:
    print(i)
    
init = []
for i in data:
    for q in i[1]:
        if(q not in init):
            init.append(q)
init = sorted(init)
print("\nItems:",init)

sp = 0.4
s = int(sp*len(init))
print("\nMinimum_Support_Count:",s)


from collections import Counter
c = Counter()
for i in init:
    for d in data:
        if(i in d[1]):
            c[i]+=1
print("\nC1:")

for i in c:
    print(str([i])+": "+str(c[i]))
print()

l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
        
print("\nL1:")
for i in l:
    print(str(list(i))+": "+str(l[i]))
print()

pl = l
pos = 1
for count in range (2,1000):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in data:
            temp = set(q[1])
            if(i.issubset(temp)):#checks whether i that is 2 items set is subset of first set of items in data
                c[i]+=1
                
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
            
    print("L"+str(count)+":")
    for i in l:
        print(str(list(i))+": "+str(l[i]))
    print()
    
    if(len(l) == 0):
        break
    pl = l
    pos = count
    
print("\nResult: ")
print("L"+str(pos)+":")
for i in pl:
    print(str(list(i))+": "+str(pl[i]))
print()
