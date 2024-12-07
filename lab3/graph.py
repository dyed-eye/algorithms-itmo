import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_graph(nodes, edges):
    G = nx.Graph()
    for i, (x, y) in enumerate(nodes):
        G.add_node(i, pos=(x, y))
    G.add_edges_from(edges)
    return G

def plot_graph(G, image_path, congestion_info, edge_width=1):
    pos = nx.get_node_attributes(G, 'pos')
    pos_inverted = {k: (v[0], v[1]) for k, v in pos.items()}
    
    img = np.flipud(plt.imread(image_path))
    plt.imshow(img, extent=[0, img.shape[1], 0, img.shape[0]])
    
    congestion_levels = [info[2] for info in congestion_info]
    max_congestion = max(congestion_levels) if congestion_levels else 1
    normalized_congestion = [level / max_congestion for level in congestion_levels]

    cmap = plt.get_cmap('Reds')
    edge_colors = [cmap(level) for level in normalized_congestion]

    nx.draw(G, pos_inverted, with_labels=True, node_color='red', edge_color=edge_colors, node_size=300, width=edge_width)
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, max_congestion))
    sm.set_array([])
    plt.colorbar(sm, label='Congestion Level (%)')

    plt.gca().invert_yaxis()
    plt.show()


def load_graph(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            edges.append((u, v))
    return edges

def load_nodes(filename):
    nodes = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(', '))
            nodes.append((x, y))
    return nodes
