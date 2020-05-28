import networkx as nx
import numpy as np
import matploblib.pyplot as plt
import pygraphviz 
from networkx.drawing.nx_agraph import graphviz_layout, write_dot

GLOBAL_PR = np.ones(G.number_of_nodes())
d = 0.8

def download_data(link):
    !wget link
    
    input = gzip.GzipFile("facebook_combined.txt.gz", 'rb')
    s = input.read()
    input.close()

    output = open("facebook_combined.txt", 'wb')
    output.write(s)
    output.close()
    
    
def readAndOpenData():
    fb_datalist = []

    with open("facebook_combined.txt", 'r') as file:
        for line in file:
            fbtuple = tuple(int(el) for el in line.split(' '))
            fb_datalist.append(mytuple)
    G=nx.Graph()
    G.clear()
    G.add_edges_from(fb_datalist)
    graph = nx.draw(G, pos=graphviz_layout(G), with_labels=True, node_size=30, width=.05)
    in_deg_vec = np.array([G.degree(n) for n in G.nodes()])
    max_ind_deg = in_deg_vec.max()

    print(in_deg_vec)
    print(max_ind_deg)
    G.degree(107)
    
    return graph


def rank_pages(graph, no_it=100):
    for _ in range(no_it):
        for node in graph.nodes:
            edges_in = [t[0] for t in graph.edges(node)]
            sum_in = 0
            for in_node in edges_in:
                c = len(graph.edges(in_node))
                pr = GLOBAL_PR[in_node]
                sum_in += pr / c
            sum_in *= d
            new_rank = sum_in + ((1 - d) / len(GLOBAL_PR))
            GLOBAL_PR[node] = new_rank


