import math
l=[]
sym=[]
w=[]
f=0
fil = open('edge.txt','r')
for n in fil:
    if(f==0):
 
        for i in range(int(n)):
            l.append([])
            sym.append([])
            l[i].append(i)
        f=1  
    else:
        r=[int(x) for x in n.split()]
        w.append([r[0],r[1]])
        l[r[0]].append(r[1])
        l[r[1]].append(r[0])
    
    

fil.close()  
    
#print(l)
#print(w)
for i in range(len(w)):
    a=len(list(set(l[w[i][0]]) & set(l[w[i][1]])))
    b=len(l[w[i][0]])
    f=len(l[w[i][1]])
    c=a/(math.sqrt(b*f))
    w[i].append(c)
    sym[w[i][0]].append([w[i][1],c])
    sym[w[i][1]].append([w[i][0],c])
comm=[]
w=sorted(w, key=lambda x:x[2],reverse=True)
#print(w)
#print(sym)
for i in range(len(l)):
    comm.append(-1)
g=0

for i in range(len(w)):
    a=w[i][0]
    b=w[i][1]
    
    if(comm[a]>-1 and comm[b]>-1):
        sym[a]=[subl for subl in sym[a] if subl[0] != b]
        sym[b]=[subl for subl in sym[b] if subl[0] != a]
        continue
    c=max(sym[a], key=lambda x: x[1])
    d=max(sym[b], key=lambda x: x[1])
    #print(a,b,c,d)
    if(c[1]==d[1]  ):
        if(comm[a]>-1):
            comm[b]=comm[a]
	        
        if(comm[b]>-1):
            comm[a]=comm[b]
	        
        else:
            comm[a]=g 
            comm[b]=g 
            g+=1 
	        
        sym[a]=[subl for subl in sym[a] if subl[0] != b]
        sym[b]=[subl for subl in sym[b] if subl[0] != a]

    
        
for i in range(len(l)):
    if(comm[i]==-1):
        comm[i]=g 
        g+=1 
        
community_list=[]
for i in range(g):  
    community_list.append([])
for i in range(len(l)):
    community_list[comm[i]].append(i)
print(community_list)    
    
    
    
    
    
    

    
    
