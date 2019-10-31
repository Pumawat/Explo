#TUNGraph: undirected graph (single edge between an unordered pair of nodes)
#TNGraph: directed graph (single directed edge between an ordered pair of nodes)
#TNEANet: directed multigraph with attributes for nodes and edges

import snap
import networkx as nx
import matplotlib.pyplot as plt

G1 = snap.LoadEdgeListStr(snap.PUNGraph, "new.txt", 1, 0)
print "Number of Nodes: %d" % G1.GetNodes()

for NI in G1.Nodes():
    print "node id %d with degree %d" % (
        NI.GetId(), NI.GetDeg())
print "praveen"
for EI in G1.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

print "praveen"
total_no_of_communities=0
community_list = {1:[],2:[],3:[]}
SubG = snap.GetSubGraph(G1, snap.TIntV.GetV(0,1,2,3,4))
for EI in SubG.Nodes():
    print "Node - %d" % (EI.GetId())

















































'''
# generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
G8 = snap.GenPrefAttach(1000, 3)
# vector of pairs of integers (size, count)
CntV = snap.TIntPrV()
# get distribution of connected components (component size, count)
snap.GetWccSzCnt(G8, CntV)
# get degree distribution pairs (degree, count)
snap.GetOutDegCnt(G8, CntV)
# vector of floats
EigV = snap.TFltV()
# get first eigenvector of graph adjacency matrix
snap.GetEigVec(G8, EigV)
# get diameter of G8
snap.GetBfsFullDiam(G8, 100)
# count the number of triads in G8, get the clustering coefficient of G8
snap.GetTriads(G8)
snap.GetClustCf(G8)
'''

'''
GetId(): return node id
GetOutDeg(): return out-degree of a node
GetInDeg(): return in-degree of a node
GetOutNId(e): return node id of the endpoint of e-th out-edge
GetInNId(e): return node id of the endpoint of e-th in-edge
IsOutNId(int NId): do we point to node id n
IsInNId(n): does node id n point to us
IsNbrNId(n): is node n our neighbor
'''