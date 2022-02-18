# Network Visualization

# A graph is the abstract, mathematical representation of a network (such as a road network in real life). Graphs are collections of vertices (nodes) and edges (links).
# A path is a sequence of unique vertices, such that any two vertices in the sequence are connected by an edge; the length of a path is the number of edges in that path.
# A graph is said to be connected if every vertex is reachable from every other vertex.

# In this Python project I import the NetworkX module, which contains many type of random graph generators, but also a few empirical datasets, and pick the Karate Club one.
# My goal is to visualize the graph, and to do so I use the nx.draw function. 

# We can randomply sample a graph from a collection of random graphs. The simplest possible random graph model is the Erdos-Renyi model (ER graph model).
# It has 2 parameters: N = number of nodes, p = probability of a pair of nodes to be connected; if p is large, graphs tend to be densely connected.
