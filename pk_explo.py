import math
import snap
import networkx as nx
import matplotlib.pyplot as plt

G1 = snap.LoadEdgeListStr(snap.PUNGraph, "new.txt", 1, 0)
total_no_of_communities=0
community_list = [[0,1,2,3],[4],[5,6,7]]
sym = [[[1, 0.8660254037844387], [3, 0.75], [2, 1.0]], [[0, 0.8660254037844387], [2, 0.8660254037844387]], [[0, 1.0], [1, 0.8660254037844387], [3, 0.75]], [[0, 0.75], [2, 0.75], [4, 0.5773502691896258]], [[3, 0.5773502691896258], [5, 0.5773502691896258]], [[4, 0.5773502691896258], [6, 0.8660254037844387], [7, 0.8660254037844387]], [[5, 0.8660254037844387], [7, 1.0]], [[6, 1.0], [5, 0.8660254037844387]]]
similarity_score = []
selected_seeds = []
priority_seeds = []
final_seed = []
degree_score = []
pq_candidate_nodes =[]
hub_seeds = [] 

for i in range(len(sym)):
	sum_of_sym=0
	for j in range(len(sym[i])):
		sum_of_sym = sum_of_sym + sym[i][j][1]
	similarity_score.append(sum_of_sym)

for NI in G1.Nodes():
    degree_score.append(NI.GetDeg())

for EI in G1.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

print "sum of similarity scores of every node"
for i in range(len(similarity_score)):
	print (similarity_score[i]),

print "\n\ndegree score of every node"
for i in range(len(degree_score)):
	print (degree_score[i]),

for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		for k in range(j+1,len(community_list[i])):
			if(degree_score[community_list[i][k]]>degree_score[community_list[i][j]]):
				temp=community_list[i][k]
				community_list[i][k]= community_list[i][j]
				community_list[i][j] = temp

			if(degree_score[community_list[i][k]]==degree_score[community_list[i][j]]):
				if(similarity_score[community_list[i][k]]>similarity_score[community_list[i][k]]):
					temp=community_list[i][k]
					community_list[i][k]= community_list[i][j]
					community_list[i][j] = temp


print "\n\npriority wise nodes in community"
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (community_list[i][j]),
	print

print "\n\ndigree score of community list"
for i in range(len(community_list)):
	for j in range(len(community_list[i])):
		print (degree_score[community_list[i][j]]),
	print


for i in range(len(community_list)):
	selected_seeds.append([])
	priority_seeds.append([])
	l=int(math.ceil(len(community_list[i])*0.1))
	for j in range(int(math.ceil(len(community_list[i])*0.1))):
		selected_seeds[i].append(community_list[i][j])
		priority_seeds[i].append(l)
		l=l-1
		

print "\n\nselected candidate seeds, community wise"
for i in range(len(selected_seeds)):
	for j in range(len(selected_seeds[i])):
		print (selected_seeds[i][j]),
	print

print "\npriority of candidate seeds"
for i in range(len(priority_seeds)):
	for j in range(len(priority_seeds[i])):
		print (priority_seeds[i][j]),
	print