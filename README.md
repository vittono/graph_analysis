# Network Visualization
A graph is the abstract, mathematical representation of a network (such as a road network in real life). Graphs are collections of vertices (nodes) and edges (links).
A path is a sequence of unique vertices, such that any two vertices in the sequence are connected by an edge; the length of a path is the number of edges in that path.
A graph is said to be connected if every vertex is reachable from every other vertex. The degree of a vertex is the number of entries connected to it.
In this Python project I am importing the NetworkX module, which contains many type of random graph generators, but also a few empirical datasets, and pick the Karate Club one.
I visualize the graph with the nx.draw function. Later I randomly sample a graph from a collection of random graphs; the easiest one is the Erdos-Rényi (ER) graph model; it has 2 parameters, N = number of nodes, p = probability of a pair of nodes to be connected. If p is large, graphs tend to be densely connected. I explicitly write my ER function to better understand the model. 
