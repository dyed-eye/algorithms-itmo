import matplotlib.pyplot as plt
import networkx as nx

def create_graph(nodes, edges):
    G = nx.Graph()
    for i, (x, y) in enumerate(nodes):
        G.add_node(i, pos=(x, y))
    G.add_edges_from(edges)
    return G

def save_graph(G, filename):
    with open(filename, 'w') as f:
        for edge in G.edges():
            f.write(f"{edge[0]} {edge[1]}\n")

def plot_graph(G, image_path, edge_width=1):
    pos = nx.get_node_attributes(G, 'pos')
    pos_inverted = {k: (v[0], v[1]) for k, v in pos.items()}
    
    img = plt.imread(image_path)
    plt.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])  # Set extent to match the image
    nx.draw(G, pos_inverted, with_labels=True, node_color='red', edge_color='black', node_size=300, width=4)
    #plt.gca().invert_yaxis()  # Invert the y-axis
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

def main(image_path, graph_file, nodes_file):
    nodes = load_nodes(nodes_file)
    edges = load_graph(graph_file)
    G = create_graph(nodes, edges)
    plot_graph(G, image_path)

if __name__ == "__main__":
    main('map.png', 'graph.txt', 'nodes.txt')
