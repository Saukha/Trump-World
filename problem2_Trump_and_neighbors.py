
# coding: utf-8

# In[37]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
from networkx.algorithms import community

G=nx.read_graphml("Problem2-TrumpWorld.graphml")

Trump_neighbors=G.neighbors('DONALD J. TRUMP')
Trump_list=[node for node in Trump_neighbors]+['DONALD J. TRUMP']
#print (len(Trump_list))
H=nx.subgraph(G,Trump_list)
degree = nx.degree(H) # degree of nodes
#print('degrees =',degree)
node_list = [n for (n,m) in degree]
degree_list = [int(m) for (n, m) in degree]

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
print(' ')
print('Trump and His Direct Neighbors')
print(nx.info(H))
nx.draw_kamada_kawai(H, with_labels=None,nodelist=node_list,node_size=[n*30 for n in degree_list])
plt.show()
plt.close()

