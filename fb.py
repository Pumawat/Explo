import networkx as nx
import matplotlib.pyplot as plt
g=nx.read_edgelist('pk.txt',create_using=nx.Graph(), nodetype=int )
color_map = []
for i in range(4039):
	if(i>1000):
		color_map.append(0)
	else:
		color_map.append(1)
print nx.info(g)
sp=nx.spring_layout(g)
plt.axis('off')
nx.draw_networkx(g,pos=sp,with_labels=True,node_size=500)
plt.show()


import numpy as np
nn = len(g.nodes)
mat = np.empty((nn, nn), dtype=float)
mat.fill(-100.0)
np.fill_diagonal(mat, -0.0)


preds = nx.jaccard_coefficient(g, g.edges)
for u, v, j in preds:
    mat[u,v] = -100 * (1 - j)

from sklearn.cluster import AffinityPropagation
np.median(mat)
af = AffinityPropagation(preference=-100, affinity="precomputed")
lab = af.fit_predict(mat)
len(np.unique(lab))

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.figure(figsize=(15,6))
pd.value_counts(lab).plot.bar()
plt.xticks([])
plt.show()

import community
import collections

partition = community.best_partition(g)
values = [partition.get(node) for node in g.nodes()]
counter=collections.Counter(values)
print(counter)

sp = nx.spring_layout(g)
nx.draw_networkx(g, pos=sp, with_labels=True, node_size=400, node_color=color_map)
#plt.axes('off')
plt.show()