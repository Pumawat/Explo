from rpy2.robjects.packages import importr
diffuse = importr("diffusr")
import rpy2.robjects as ro
import snap
import heapq
from numpy import array


threshold = 10
no_of_sig_com = 3
amount = 20
N = 8
E = 10
graph = snap.TUNGraph.New(N,E)

community_list = {1:[1,2,5,8],2:[3,4,6],3:[7]}
selected_seeds = {1:[[1,8],[2,7],[5,6],[8,5]],2:[[3,8],[4,7],[6,5]],3:[[7,8]]}
final_seed_global = [1,3,7]
pq_candidate_nodes = {1:[],2:[],3:[]}
pq_sel_nodes = {1:[],2:[],3:[]}
time = 20
hub_seeds = []
edges = {1:[2,8],2:[1,8,5],3:[4,6],4:[3,6],5:[2,8],6:[7,3,4],7:[8,6],8:[1,2,5,7]}

def build_graph():
    for i in range(1,9):
        graph.AddNode(i)
    for key in edges:
        for dest in edges[key]:
            graph.AddEdge(key,dest)
            graph.AddEdge(dest,key)
#     for i in graph.Edges():
#         print "edge (%d, %d)" % (i.GetSrcNId(), i.GetDstNId())
   
   

def build_pq():
    for community in selected_seeds:
        for node_one in selected_seeds[community]:
           
#             print("this is ")
#             print(node_one)
#             print(type(node_one))
#             print(node[0])
            if node_one[0] in final_seed_global:
                heapq.heappush(pq_sel_nodes[community],node_one[1])
            else:
                heapq.heappush(pq_candidate_nodes[community],-node_one[1])
       
    for key in pq_sel_nodes:
        heapq.heapify(pq_sel_nodes[key])
        heapq.heapify(pq_candidate_nodes[key])


def adj_cal():
    adj = []
    for i in range(N):
        new = []
        for j in range(N):
            new.append(0)
        adj.append(new)
    edge_itr = graph.BegEI()
    for i in range(E):
        (p,q) = edge_itr.GetId()
        if(i != E-1):
            edge_itr.Next()
        adj[p-1][q-1] = 1
        adj[q-1][p-1] = 1
#     a = array(adj)
#     print(a.shape)
#     print(adj)
    r_adj = ro.r.matrix(ro.IntVector([j for sub in adj for j in sub]), nrow = 8)
    return r_adj
        
def start_vector_cal(tmp_final_seed):
    vector = [0 for i in range(N)]
    for i in tmp_final_seed:
            vector[i-1] = amount
    for i in hub_seeds:
        vector[i-1] = amount
#     print("start_vector")
#     print(vector)
    r_vector = ro.r.matrix(ro.IntVector(vector),nrow = 8)
    return r_vector
   

def activate_node_cal(result):
    count = 0
#     print(result)
    for i in range(N):
            if(result[i]>threshold):
                count += 1
    return count

def calculate_max_left(result):
    max_left = 1
    count = 0
    max_count = 0
#     print("pq_candidate_nodes")
#     print(pq_candidate_nodes)
#     print("pq_sel_nodes")
#     print(pq_sel_nodes)
    for community in community_list:
        count = 0
        for node in community_list[community]:
#             print("node")
#             print(node)
            if(result[node-1]<threshold):
                count += 1
#         print("count of ")
#         print(community)
#         print(count)
        if count>max_count:
            max_left = community
            max_count = count
#     print("max left")
#     print(max_left)
    prior = heapq.heappop(pq_candidate_nodes[max_left])
    for node in selected_seeds[max_left]:
#             print("node")
#             print(node)
        if(node[1] == -prior):
            add_node = node[0]
       
    return add_node

def calculate_min_load():
    min_load_community = 1
    min_load = 1000000000
    size_of_seed = 0
    for community in community_list:
        size_of_seed = 0
        size_of_community = len(community_list[community])
        for final in final_seed_global:
#             print("final")
#             print(final)
            if final in community_list[community]:
                size_of_seed += 1
           
       
#         print("community")
#         print(community)
       
#         print("size of community")
#         print(size_of_community)
#         print("size of seed")
#         print(size_of_seed)
        load = size_of_community/size_of_seed
#         print("load of")
#         print(community)
#         print(load)
        if load<min_load:
            min_load_community = community
#         print("min load community")
#         print(min_load_community)
        prior = heapq.heappop(pq_sel_nodes[min_load_community])
        for node in selected_seeds[min_load_community]:
                if(node[1] == prior):
                    remove_node = node[0]
        heapq.heappush(pq_candidate_nodes[community],-node_one[1])
                   
    return remove_node
           
   

def seed_tuning():
    r_adj = adj_cal()
    r_start_vector = start_vector_cal(final_seed_global)
    result = diffuse.heat_diffusion(r_start_vector,r_adj,t = 100)
    build_pq()
    max_no_activated_nodes = activate_node_cal(result)
    print("at 0 seeds are")
    print(final_seed_global)
    for i in range(10):
        print("at iteration")
        print(i)
        tmp_final_seed = final_seed_global
        delete_node = calculate_min_load()
       
        add_node = calculate_max_left(result)
        print("add node is")
        print(add_node)
       
        print("delete node")
        print(delete_node)
        tmp_final_seed.remove(delete_node)
        tmp_final_seed.append(add_node)
        result = diffuse.heat_diffusion(start_vector_cal(tmp_final_seed),r_adj,t = time)
        no_activated_nodes = activate_node_cal(result)
        if(no_activated_nodes > max_no_activated_nodes):
            max_no_activated_nodes = no_activated_nodes
            final_seed = tmp_final_seed
    print(final_seed)


build_graph()
# print(final_seed)
seed_tuning()

    
    
    
