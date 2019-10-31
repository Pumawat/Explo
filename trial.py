import snap
import networkx as nx
import matplotlib.pyplot as plt
g=nx.read_edgelist('new.txt',create_using=nx.Graph(), nodetype=int )
print nx.info(g)
n=g.nodes();
e=g.edges();
for i in n:
	print (i),
print 
for i in e:
	print (i),

print
print

#G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
# traverse the nodes
for NI in g.nodes():
    print "node id %d with out-degree %d and in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
# traverse the edges
for EI in g.edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
# traverse the edges by nodes
for NI in g.nodes():
    for Id in NI.GetOutEdges():
        print "edge (%d %d)" % (NI.GetId(), Id)

