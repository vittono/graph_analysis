# graph is the abstract, mathematical representation of a network (such as a road network in real life)
# graphs are collections of vertices (nodes) and edges (links)
# a path is a sequence of unique vertices, such that any two vertices in the sequence are connected by an edge
# length of a path is the number of edges in that path
# a graph is said to be connected if every vertex is reachable from every other vertex

import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

K = nx.karate_club_graph()
nx.draw(K, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")
K.degree()[33]   # K.degree() treated as a dictionary
K.degree(33)   # K.degree() treated as a method

# we can sample random graphs from a collection of random graphs
# simplest possible random graph model is the Erdos-Renyi model (ER graph model)
# it has 2 parameters, N = number of nodes, p = probability of a pair of nodes to be connected
# if p is large, graphs tend to be densely connected

bernoulli.rvs(p=0.2)
N = 20
p = 0.2


def er_graph(N, p):
    """generates an ER graph"""
    # create empty graph
    g = nx.Graph()
    # add all N nodes in the graph
    g.add_nodes_from(range(N))
    # loop over all pairs of nodes
    for node1 in g.nodes():
        for node2 in g.nodes():
            # add an edge with probability = p
            if node1 < node2 and bernoulli.rvs(p=p):
                g.add_edge(node1, node2)
    # print(g.number_of_nodes())
    # nx.draw(g)
    return g


nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")


def plot_degree_distribution(g):
    degree_sequence = [d for n, d in g.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")


G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.pdf")

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist3.pdf")

E1 = nx.erdos_renyi_graph(100, 0.03)
plot_degree_distribution(E1)
E2 = nx.erdos_renyi_graph(100, 0.30)
plot_degree_distribution(E2)
