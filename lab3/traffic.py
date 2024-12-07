import networkx as nx
import random


def simulate_traffic(G, num_cars, peak_hours):
    traffic_data = {edge: 0 for edge in G.edges()}
    for _ in range(num_cars):
        start = random.choice(list(G.nodes()))
        end = random.choice(list(G.nodes()))
        if start != end:
            path = nx.shortest_path(G, source=start, target=end)
            for i in range(len(path) - 1):
                edge = (path[i], path[i + 1])
                # Ensure the edge exists in traffic_data
                if edge in traffic_data:
                    traffic_data[edge] += 1
                else:
                    # If the graph is undirected, check the reverse edge
                    reverse_edge = (path[i + 1], path[i])
                    if reverse_edge in traffic_data:
                        traffic_data[reverse_edge] += 1
                    else:
                        print(f"Warning: Edge {edge} not found in traffic_data.")
    return traffic_data

def calculate_congestion(G, traffic_data):
    congestion_info = []
    for edge in G.edges(data=True):
        num_cars = traffic_data[edge[:2]]
        capacity = edge[2].get('capacity', 10)  # Default capacity if not set
        congestion_percentage = (num_cars / capacity) * 100 if capacity > 0 else 0
        congestion_info.append((edge[:2], num_cars, congestion_percentage))
    return congestion_info

def identify_top_congested(congestion_info):
    return sorted(congestion_info, key=lambda x: x[2], reverse=True)[:10]
