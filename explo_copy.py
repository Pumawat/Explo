import math
import snap
import networkx as nx
import matplotlib.pyplot as plt

l=[]
sym=[]
w=[]
similarity_score = []
community_list=[]
selected_seeds = []
priority_seeds = []
final_seed = []
degree_score = []
pq_candidate_nodes =[]
hub_seeds = []
comm=[] 
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
# print "\n\n"
# print(w)
# print "\n\n" 
# print(l)
# print "\n\n"
for i in range(len(l)):
	degree_score.append(len(l[i])-1)

# print degree_score

for i in range(len(w)):
	a=len(list(set(l[w[i][0]]) & set(l[w[i][1]])))
	b=len(l[w[i][0]])
	f=len(l[w[i][1]])
	c=a/(math.sqrt(b*f))
	w[i].append(c)
	sym[w[i][0]].append([w[i][1],c])
	sym[w[i][1]].append([w[i][0],c])


w=sorted(w, key=lambda x:x[2],reverse=True)

for i in range(len(sym)):
	sum_of_sym=0
	for j in range(len(sym[i])):
		sum_of_sym = sum_of_sym + sym[i][j][1]
	similarity_score.append(sum_of_sym)

# print ("sum of similarity scores of every node")
# print (similarity_score)
# print "\n"

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
		


for i in range(g):  
	community_list.append([])

for i in range(len(l)):
	community_list[comm[i]].append(i)
'''
print community_list

print ("\n\nnodes community wise")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (community_list[i][j]+1),
	print

print ("\n\ndigree score of community list")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (degree_score[community_list[i][j]]),
	print


print ("\n\ndegree score of every node")
for i in range(len(degree_score)):
	print (degree_score[i]),

print ("\n\nsum of symmilarity score of community list")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (similarity_score[community_list[i][j]]),
	print
'''

for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		for k in range(j+1,len(community_list[i])):
			if(degree_score[community_list[i][k]]>degree_score[community_list[i][j]]):
				temp = community_list[i][k]
				community_list[i][k] = community_list[i][j]
				community_list[i][j] = temp
			elif(degree_score[community_list[i][k]]==degree_score[community_list[i][j]]) and (similarity_score[community_list[i][k]]>similarity_score[community_list[i][j]]):
				temp = community_list[i][k]
				community_list[i][k] = community_list[i][j]
				community_list[i][j] = temp

'''			
print ("\n\npriority wise nodes in community")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (community_list[i][j]+1),
	print

print ("\n\ndigree score of community list")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (degree_score[community_list[i][j]]),
	print

print ("\n\nsum of symmilarity score of community list")
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (similarity_score[community_list[i][j]]),
	print
'''

for i in range(len(community_list)):
	selected_seeds.append([])
	priority_seeds.append([])
	l=int(math.ceil(len(community_list[i])*0.1))
	for j in range(int(math.ceil(len(community_list[i])*0.1))):
		selected_seeds[i].append(community_list[i][j]+1)
		priority_seeds[i].append(l)
		l=l-1
		

print ("selected candidate seeds, community wise")
for i in range(len(selected_seeds)):
	for j in range(len(selected_seeds[i])):
		print (selected_seeds[i][j]),
	print

'''
print ("\npriority of candidate seeds")
for i in range(len(priority_seeds)):
	for j in range(len(priority_seeds[i])):
		print (priority_seeds[i][j]),
	print
'''