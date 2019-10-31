import math
# import snap
import time
# import networkx as nx
# import matplotlib.pyplot as plt
start = time.time()
l=[]
sym=[]
sym1=[]
score=[]
w=[]
tot_simm=0
similarity_score = []
community_list_intial=[]
selected_seeds_intial = []
priority_seeds = []
# final_seed = []
degree_score = []
# pq_candidate_nodes =[]
hub_seeds = []
comm=[]
f=0
fil = open('edge.txt','r')
for n in fil:
    if(f==0):
 
        for i in range(int(n)):
            l.append([])
            sym.append([])
            sym1.append([])
            l[i].append(i)
        f=1  
    else:
        r=[int(x) for x in n.split()]
        
        w.append([r[0],r[1]])
        l[r[0]].append(r[1])
        l[r[1]].append(r[0])
    
    

fil.close()  
for i in range(len(l)):
    degree_score.append(len(l[i])-1)  

#print(w)
#print(len(w))

score=[]
for i in range(len(w)):
    a=len(list(set(l[w[i][0]]) & set(l[w[i][1]])))
    b=len(l[w[i][0]])
    f=len(l[w[i][1]])
    c=a/(math.sqrt(b*f))
    tot_simm+=c
    score.append(c)
    w[i].append(c)
    sym[w[i][0]].append([w[i][1],c])
    sym[w[i][1]].append([w[i][0],c])
    sym1[w[i][0]].append([w[i][1],c])
    sym1[w[i][1]].append([w[i][0],c])
comm=[]
score=list(set(score))
score=sorted(score, reverse=True)
v=0
#print(w)
#print(sym)

for i in range(len(l)):
    comm.append(i)
q_prev=-100    
while(1):
    prev_comm=comm
    for i in range(len(w)):
        a=w[i][0]
        b=w[i][1]
        
    
        
        if(comm[a]==comm[b]):
            continue
            
          
        c=max(sym[a], key=lambda x: x[1])
        d=max(sym[b], key=lambda x: x[1])
        #print(a,b,c,d)
        if(c[1]==d[1] and c[1]==score[v]):
            
            g=comm.count(comm[a])
            h=comm.count(comm[b])
            f=comm[a]
            k=comm[b]
            if(g>h):
                for i in range(len(comm)):
                    if(comm[i]==k):
                        comm[i]=f
                
            else:
                for i in range(len(comm)):
                    if(comm[i]==f):
                        comm[i]=k
            sym[a]=[subl for subl in sym[a] if subl[0] != b]
            sym[b]=[subl for subl in sym[b] if subl[0] != a]

    q_curr=0 
    v+=1
    r=list(set(comm))
    
    for i in r:
        IS=0
        DS=0
        
        for j in range(len(l)):
            for k in range(j+1,len(l)):
                if(comm[j]==comm[k] and comm[j]==i):
                    t=sym1[j]
                    
                    for e in t:
                        if(e[0]==k):
                            IS+=e[1]
        for j in range(len(l)):
            if(comm[j]==i):
                
                for k in range(len(l)):
                    if(comm[k]!=i):
                        
                        q=sorted([j,k])
                        
                        for y in w:
                            if(y[0]==q[0] and y[1]==q[1]):
                        
                                t=sym1[q[0]]
                                
                                for e in t:
                                    if(e[0]==q[1]):
                                        DS+=e[1]
                                
              
                      
        q_curr+=((IS/tot_simm)-((DS/tot_simm)**2))  
        
    
    if((q_curr-q_prev)<=0):
        comm=prev_comm
        break
    else:
        prev_comm=comm 
        q_prev=q_curr
                    
community_list_initial=[]
for i in range(len(l)):
    community_list_initial.append([])
for i in range(len(l)):
    a=comm[i]
    community_list_initial[a].append(i)
community_list_initial=[subl for subl in community_list_initial if len(subl)!=0]
          


     

    
    
# print community_list_intial

# print ("\n\nnodes community wise")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (community_list_intial[i][j]),
#     print

# print ("\n\ndigree score of community list")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (degree_score[community_list_intial[i][j]]),
#     print


# print ("\n\ndegree score of every node")
# for i in range(len(degree_score)):
#     print (degree_score[i]),

# print ("\n\nsum of symmilarity score of community list")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (similarity_score[community_list_intial[i][j]]),
#     print


for i in range(len(community_list_intial)):
    for j in range(len(community_list_intial[i])):
        for k in range(j+1,len(community_list_intial[i])):
            if(degree_score[community_list_intial[i][k]]>degree_score[community_list_intial[i][j]]):
                temp = community_list_intial[i][k]
                community_list_intial[i][k] = community_list_intial[i][j]
#                 print ("ers")
                community_list_intial[i][j] = temp
            elif(degree_score[community_list_intial[i][k]]==degree_score[community_list_intial[i][j]]) and ((similarity_score[community_list_intial[i][k]])>similarity_score[community_list_intial[i][j]]):
                temp = community_list_intial[i][k]
                community_list_intial[i][k] = community_list_intial[i][j]
#                 print ("praveen")
                community_list_intial[i][j] = temp

# print ("\n\npriority wise nodes in community")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (community_list_intial[i][j]),
#     print

# print ("\n\ndigree score of community list")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (degree_score[community_list_intial[i][j]]),
#     print

# print ("\n\nsum of symmilarity score of community list")
# for i in range(len(community_list_intial)):
#     for j in range(len(community_list_intial[i])):
#         print (similarity_score[community_list_intial[i][j]]),
#     print

for i in range(len(community_list_intial)):
    selected_seeds_intial.append([])
    priority_seeds.append([])
    l=int(math.ceil(len(community_list_intial[i])*0.1))
    for j in range(int(math.ceil(len(community_list_intial[i])*0.1))):
        selected_seeds_intial[i].append(community_list_intial[i][j])
        priority_seeds[i].append(l)
        l=l-1
       

print ("\n\nselected candidate seeds, community wise")
for i in range(len(selected_seeds_intial)):
    for j in range(len(selected_seeds_intial[i])):
        print (selected_seeds_intial[i][j]),
    print

# print ("\npriority of candidate seeds")
# for i in range(len(priority_seeds)):
#     for j in range(len(priority_seeds[i])):
#         print (priority_seeds[i][j]),
#     print
# print selected_seeds_intial
# print community_list_intial


end = time.time()
print("Running time")
print(end-start)
print(community_list_intial)
print(selected_seeds_intial)
from rpy2.robjects.packages import importr
diffuse = importr("diffusr")
import rpy2.robjects as ro
import snap
import heapq
from numpy import array
import copy
import networkx as nx
import time
import matplotlib.pyplot as plt
start_2 = time.time()
# from intial import *
# from intial import community_list_intial,selected_seeds
#from intial import new
# new()
threshold = 5
no_of_sig_com = 9
amount = 20
N = 0
E = 0
# cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']
# graph = snap.TUNGraph.New(N,E)




# community_list = {1:[1,2,5,8],2:[3,4,6],3:[7]}
# selected_seeds = {1:[[1,8],[2,7],[5,6],[8,5]],2:[[3,8],[4,7],[6,5]],3:[[7,8]]}
# final_seed_global = [1,3,7]
# pq_candidate_nodes = {1:[],2:[],3:[]}
# pq_sel_nodes = {1:[],2:[],3:[]}
community_list = dict()
selected_seeds = dict()
final_seed_global = [item for l in selected_seeds_intial for item in l]
# print(final_seed_global)
pq_candidate_nodes = dict()
pq_sel_nodes = dict()
node = []
color_map = []
color_map_com = []
graph = nx.Graph()




time_p = 2

hub_seeds = []
fig_size = [0,0]
fig_size[0] = 10
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size
# edges = {1:[2,8],2:[1,8,5],3:[4,6],4:[3,6],5:[2,8],6:[7,3,4],7:[8,6],8:[1,2,5,7]}

# def build_graph():
#     global N
#     global E
#     checker = 0
#     for i in open('edge.txt'):
#         if checker != 0:
#             j = i.split()
#             src = int(j[0])
#             dest = int(j[1])
#             if src not in node:
#                 graph.AddNode(src)
#                 node.append(src)

#             if dest not in node:
#                 graph.AddNode(dest)
#                 node.append(dest)
#             graph.AddEdge(src,dest)
#             graph.AddEdge(dest,src)
#         checker = 1
#     for e in graph.Edges():
#         E += 1
#     for n in graph.Nodes():
#         N += 1
#     print "N"
#     print(N)
#     print "E"
#     print(E)

# def adj_cal():
#     adj = []
#     print N
#     for i in range(N):
#         new = []
#         for j in range(N):
#             new.append(0)
#         adj.append(new)
#     edge_itr = graph.BegEI()
#     for i in range(E):
#         (p,q) = edge_itr.GetId()
#         if(i != E-1):
#             edge_itr.Next()
#         adj[p-1][q-1] = 1
#         adj[q-1][p-1] = 1
#     print adj
#     r_adj = ro.r.matrix(ro.IntVector([j for sub in adj for j in sub]), nrow = N)
#     return r_adj

def adj_cal():
    adj = []
    global N
    global E
    checker = 0
    for i in open('edge.txt'):
        if checker != 0:
            j = i.split()
            src = int(j[0])
            dest = int(j[1])
            E += 1
            adj[src][dest] = 1
            adj[dest][src] = 1
            graph.add_edge(src,dest)
        if checker == 0:
            N = int(i)
            E += 1
            checker = 1
           
            for i in range(N):
                color_map.append(0)
                color_map_com.append(0)
                graph.add_node(i)
                new = []
                for j in range(N):
                    new.append(0)
                adj.append(new)
#     print N
#     print adj
    r_adj = ro.r.matrix(ro.IntVector([j for sub in adj for j in sub]), nrow = N)
    return r_adj

       
def build_community_list():
    for i in range(1,len(community_list_intial)+1):
            community_list[i] = community_list_intial[i-1]

def com_visualise():
    t = 0
    for i in community_list_intial:
        t += 1
        for j in i:
            color_map_com[j] = t
    print(color_map_com)
    pos = nx.spring_layout(graph)
#     nx.draw(graph,node_color= color_map_com, node_size=100,orientation = 'landscape',dpi = 600,scale = 100,pos)
    nx.draw(graph,node_color= color_map_com, node_size=1000,orientation = 'landscape',dpi = 200,with_labels=False, font_color='white')
   
    plt.show()
   
       
   

   
   
def build_selected_seeds():
    global selected_seeds
    selected_seeds = copy.deepcopy(community_list)
    for key in selected_seeds:
        length = len(selected_seeds[key])
        for i in range(len(selected_seeds[key])):
            item = selected_seeds[key].pop(0)
            new_item = [item,length-i]
            selected_seeds[key].append(new_item)

           

def build_pq():
#     print selected_seeds
    for community in selected_seeds:
       
        pq_sel_nodes[community] = []
        pq_candidate_nodes[community] = []
       
        for node_one in selected_seeds[community]:
            if node_one[0] in final_seed_global:
                heapq.heappush(pq_sel_nodes[community],node_one[1])
            else:
                heapq.heappush(pq_candidate_nodes[community],-node_one[1])
       
    for key in pq_sel_nodes:
        heapq.heapify(pq_sel_nodes[key])
        heapq.heapify(pq_candidate_nodes[key])
#     print "after pq_build"
#     print "pq_candidate"
#     print(pq_candidate_nodes)
#     print "pq_sel_nodes"
#     print(pq_sel_nodes)


        
def start_vector_cal(tmp_final_seed):
    vector = [0 for i in range(N)]
#     print tmp_final_seed
#     print type(tmp_final_seed[0])
    for i in tmp_final_seed:
            vector[i-1] = amount
    for i in hub_seeds:
        vector[i-1] = amount
    r_vector = ro.r.matrix(ro.IntVector(vector),nrow = N)
    return r_vector


   

def activate_node_cal(result):
    count = 0
    for i in range(N):
            if(result[i]>threshold):
                count += 1
    return count
import operator

def get_key(val,dict_here):
    for key, value in dict_here.items():
         if val == value:
            return key
 
    return "key doesn't exist"
def calculate_max_left(result,l):
    max_left = 1
    count = 0
    max_count = 0
    count_dict = {}
    sorted_count = []
    for community in community_list:
        count = 0
        for node in community_list[community]:
            if(result[node-1]<threshold):
                count += 1
           
            count_dict[community] = count 
       
   
    print(count_dict)
    for t in count_dict:
            sorted_count.append(count_dict[t])
    sorted_count = sorted(sorted_count)
    print(sorted_count)
    max_count = sorted_count[l]
    max_left = get_key(max_count,count_dict)
    print("add node community is")
    print(max_left)
    print("no")
    prior = heapq.heappop(pq_candidate_nodes[max_left])
    heapq.heappush(pq_sel_nodes[max_left],-prior)
    for node in selected_seeds[max_left]:
        if(node[1] == -prior):
            add_node = node[0]
#     print "after add node pq_candidate"
#     print(pq_candidate_nodes)
#     print "after add node pq sel nodes"
#     print(pq_sel_nodes)
    return add_node

def calculate_min_load():
    global community_list
    min_load_community = 1
    min_load = 1000000000
    size_of_seed = 0
    for community in community_list:
        size_of_seed = 0
        size_of_community = len(community_list[community])
        for final in final_seed_global:
            if final in community_list[community]:
                size_of_seed += 1
        if size_of_seed > 0:
            load = size_of_community/size_of_seed
            if load<min_load:
                min_load_community = community
    print("remove node community is")
    print(min_load_community)
    prior = heapq.heappop(pq_sel_nodes[min_load_community])
    for node in selected_seeds[min_load_community]:
            if(node[1] == prior):
                remove_node = node[0]
    heapq.heappush(pq_candidate_nodes[min_load_community],-prior)
   
#     print("after remove node candidates")
#     print pq_candidate_nodes
#     print "after remove node pq sel node"
#     print pq_sel_nodes
                   
    return remove_node
           
import time          
def seed_tuning():
    adj_cal_stime = time.time()
    r_adj = adj_cal()
    adj_cal_etime = time.time()
    print("Adj calculated in time")
    print(adj_cal_etime-adj_cal_stime)
    for n1,attr in graph.nodes(data=True):
        attr['color'] = "white"
    print(n1,attr)
    start = time.time()
    r_start_vector = start_vector_cal(final_seed_global)
    end = time.time()
    print("Start vector calculated in")
    print(end-start)
    com_visualise()
    start = time.time()
    print("Result calculated in")
    result = diffuse.heat_diffusion(r_start_vector,r_adj,t = time_p)
    end = time.time()
    print(end-start)
    final_seed = final_seed_global
#     print(plt.get_clim('viridis'))
    print("at itertion 0 result")
#     print result
    build_pq()
    max_no_activated_nodes = activate_node_cal(result)
    if activate_node_cal(result) != N:
        for i in range(3):
            print("at iteration")
            print(i)
            tmp_final_seed = final_seed_global
            delete_node = calculate_min_load()

            add_node = calculate_max_left(result,i)
            print("add node is")
            print(add_node)

            print("delete node")
            print(delete_node)
            tmp_final_seed.remove(delete_node)
            tmp_final_seed.append(add_node)
            result = diffuse.heat_diffusion(start_vector_cal(tmp_final_seed),r_adj,t = time_p)
#             print "result"
#             print (result)
            no_activated_nodes = activate_node_cal(result)
            print("Number of activated nodes are: ")
            print(no_activated_nodes)
            if(no_activated_nodes > max_no_activated_nodes):
                max_no_activated_nodes = no_activated_nodes
                final_seed = tmp_final_seed
            for i in range(N):
                if(result[i]>=threshold):
                    color_map[i] = 0.4
             
                elif(result[i]<threshold):
                    color_map[i] = 0.2
            if activate_node_cal(result) == N:
                break
#             print(color_map)
            nx.draw(graph,node_color= color_map, node_size=1000,orientation = 'landscape',dpi = 200,with_labels=False, font_color='white')
            plt.show()
    print "Final seeds are"
    print(final_seed)

# print(community_list_intial)
build_community_list()
# build_graph()
build_selected_seeds()
# print "outside function selected seeds"
# print(selected_seeds)

seed_tuning()
end_2 = time.time()
print("Time taken is")
print(end_2-start_2)
# graph[0]['color'][0] = "blue"
