import math
l=[]
sym=[]
for i in range(8):
    l.append([])
    sym.append([])
    l[i].append(i)
w=[]    
for i in range(10):
    r=[int(x) for x in input().split()]
    w.append([r[0],r[1]])
    l[r[0]].append(r[1])
    l[r[1]].append(r[0])
    
#print(l)
#print(w)
for i in range(len(w)):
    a=len(list(set(l[w[i][0]]) & set(l[w[i][1]])))
    b=len(l[w[i][0]])
    f=len(l[w[i][1]])
    c=a/(math.sqrt(b*f))
    sym[w[i][0]].append([w[i][1],c])
    sym[w[i][1]].append([w[i][0],c])
comm=[]
#print(sym)
for i in range(8):
    comm.append(-1)
g=1 

for i in range(len(w)):
    a=w[i][0]
    b=w[i][1]
    if(comm[a]>0 and comm[b]>0):
        continue
    c=max(sym[a], key=lambda x: x[1])
    d=max(sym[b], key=lambda x: x[1])
    #print(a,b,c,d)
    if(c[1]==d[1]):
        if(comm[a]>0):
            comm[b]=comm[a]
        if(comm[b]>0):
            comm[a]=comm[b]
        else:
            comm[a]=g 
            comm[b]=g 
            g+=1 
        sym[a]=[subl for subl in sym[a] if subl[0] != b]
        sym[b]=[subl for subl in sym[b] if subl[0] != a]
for i in range(len(w)):
    a=w[i][0]
    b=w[i][1]
    if(comm[a]>0 and comm[b]>0):
        continue
    c=max(sym[a], key=lambda x: x[1])
    d=max(sym[b], key=lambda x: x[1])
    #print(a,b,c,d)
    if(c[1]==d[1]):
        if(comm[a]>0):
            comm[b]=comm[a]
        if(comm[b]>0):
            comm[a]=comm[b]
        else:
            comm[a]=g 
            comm[b]=g 
            g+=1 
        sym[a]=[subl for subl in sym[a] if subl[0] != b]
        sym[b]=[subl for subl in sym[b] if subl[0] != a]
        
for i in range(8):
    if(comm[i]==-1):
        comm[i]=g 
        g+=1 
        
print(comm)