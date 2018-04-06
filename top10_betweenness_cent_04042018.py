
# coding: utf-8

# In[ ]:



# coding: utf-8

# In[8]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import community
from operator import itemgetter

# draw original graph by degree
print('Trump World')
H=nx.read_graphml("problem2_TrumpWorld.graphml")

metric = 'betweenness'
#sort node_dict by centrality metric
print('Top 10 nodes by ' + metric)
centrality_dict = nx.betweenness_centrality(H)  # calculate betweennes centrality
sorted_centrality = sorted(centrality_dict.items(), key =itemgetter(1), reverse=True) 
top_nodes = sorted_centrality[:10]
node_list = [n for (n,m) in top_nodes]
node_size = [m*5000 for (n, m) in top_nodes]
#labels = dict(zip(node_list, node_list)) # create labels dictionary from node_list, node label as dict and value
labels={'DONALD J. TRUMP': 'TRUMP', 'WILBUR ROSS': 'WILBUR', 'IVANKA TRUMP': 'IVANKA', 'JARED KUSHNER': 'JARED', 'THRIVE CAPITAL': 'THRIVE CAP.', 'BETSY DEVOS': 'BETSY', 'ELAINE CHAO': 'ELAINE', 'GOLDMAN SACHS': 'GOLDMAN', '40 WALL STREET LLC': '40 WALL ST.', 'KUSHNER COMPANIES': 'KUSHNER CO.'}
print(labels)

G=nx.subgraph(H,node_list) # subgraph with only top nodes

# draw subgraph with only top nodes
plt.figure(figsize=(5,5))
nx.draw_circular(G, with_labels=True,nodelist=node_list,node_size=node_size,font_weight='normal', font_size='12')
#filename = "subgraph w top nodes by "+ metric + ".png"
#plt.savefig(filename, dpi=500)
plt.margins(0.2, 0.2)
plt.show()
plt.close()

# draw whole graph, draw and label only top nodes
plt.figure(figsize=(6,6))
pos = nx.kamada_kawai_layout(H)
nx.draw_kamada_kawai(H, with_labels=None, node_list=None, node_size =0)
nx.draw_networkx_nodes(H, pos, nodelist=node_list,node_size=node_size, alpha = 0.8, node_color='b')
nx.draw_networkx_labels(H, pos, labels=labels,font_color='r', font_weight='bold', font_size='14')
'''
nx.draw_kamada_kawai(H, with_labels=None,nodelist=node_list,node_size=node_size, alpha = 0.9, node_color='b')
nx.draw_networkx_labels(H, pos, labels=labels,font_color='r', font_weight='bold', font_size='14')
'''
#filename = "wholegraph w top nodes by "+ metric + ".png"
#plt.savefig(filename, dpi=500)
plt.margins(0.02, 0.02)
plt.show()
plt.close()
print("Top 10 nodes by " + metric)
for b in top_nodes:
    print(b)
print('  ')


