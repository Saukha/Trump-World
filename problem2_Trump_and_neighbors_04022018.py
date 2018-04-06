
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
from networkx.algorithms import community

G=nx.read_graphml("problem2_TrumpWorld.graphml")

Trump_neighbors=G.neighbors('DONALD J. TRUMP')
Trump_list=[node for node in Trump_neighbors]+['DONALD J. TRUMP']
#print (len(Trump_list))
H=nx.subgraph(G,Trump_list)
degree = nx.degree(H) # degree of nodes
#print('degrees =',degree)
node_list = [n for (n,m) in degree]
node_size = [m*30 for (n, m) in degree]
#degree_list = [m for (n, m) in degree]

'''
print('node type =',type(node_list[0]))
print('nodes = ', node_list)
print('degree type =',type(degree_list[0]))
#print('degrees =',degree_list)
print('============')

d = nx.degree(g)
nx.draw(g, nodelist=d.keys(), node_size=[v * 100 for v in d.values()])  # this didn't work
'''
print('Trump World')
print(nx.info(G))
print('average clustering coefficient =', nx.average_clustering(G))
print('average shortest path length =', nx.average_shortest_path_length(G))

print(' ')
print('Trump and His Direct Neighbors')
print(nx.info(H))
print('average clustering coefficient =', nx.average_clustering(H))
print('average shortest path length =', nx.average_shortest_path_length(H))

plt.figure(figsize=(6,6))
pos = nx.kamada_kawai_layout(H)
nx.draw_kamada_kawai(H, with_labels=None, node_list=None, node_size =0)
nx.draw_networkx_nodes(H, pos, nodelist=node_list,node_size=node_size, alpha = 0.8, node_color='r')
nx.draw_networkx_labels(H, pos, labels={'DONALD J. TRUMP': 'Trump'},font_color='b', font_weight='bold', font_size='14')


#nx.draw_kamada_kawai(H, with_labels=None,nodelist=node_list,node_size=[n*30 for n in degree_list])
plt.show()
plt.close()

