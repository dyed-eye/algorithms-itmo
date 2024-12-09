import networkx as nx
import random

def simulate_traffic(G, num_cars, peak_hours):
    traffic_data = {edge: 0 for edge in G.edges()}
    high_congestion_duration = {edge: 0 for edge in G.edges()}
    congestion_threshold = 0.9  # 90% congestion
    time_steps = 144  # 24 hours with 10-minute intervals (24 * 6 = 144)

    for t in range(time_steps):
        # Determine the number of cars based on the time of day
        hour = t // 6  # Each time step represents 10 minutes, so 6 steps per hour
        if hour in peak_hours:
            current_num_cars = int(num_cars * 1.8)
        else:
            current_num_cars = num_cars

        for _ in range(current_num_cars):
            start = random.choice(list(G.nodes()))
            end = random.choice(list(G.nodes()))
            if start != end:
                path = nx.shortest_path(G, source=start, target=end)  # Generate routes
                for i in range(len(path) - 1):
                    edge = (path[i], path[i + 1])
                    if edge in traffic_data:
                        traffic_data[edge] += 1
                    else:
                        reverse_edge = (path[i + 1], path[i])
                        if reverse_edge in traffic_data:
                            traffic_data[reverse_edge] += 1
                            
        adaptive_traffic_signals(G, traffic_data, t)                            

        for edge in G.edges():
            num_cars = traffic_data[edge]
            capacity = G[edge[0]][edge[1]].get('capacity', 10)  # Default capacity
            congestion_percentage = (num_cars / capacity) if capacity > 0 else 0
            
            if congestion_percentage > congestion_threshold:
                high_congestion_duration[edge] += 1

    return traffic_data, high_congestion_duration

def calculate_congestion(G, traffic_data, high_congestion_duration):
    congestion_info = []
    for edge in G.edges():
        num_cars = traffic_data[edge]
        capacity = G[edge[0]][edge[1]].get('capacity', 10)  # Correctly access capacity
        congestion_percentage = (num_cars / capacity) * 100 if capacity > 0 else 0
        duration_high_congestion = high_congestion_duration[edge]  # Get duration of high congestion
        congestion_info.append((edge, num_cars, congestion_percentage, duration_high_congestion))
    return congestion_info

def identify_top_congested(congestion_info):
    return sorted(congestion_info, key=lambda x: x[2], reverse=True)[:10]
    
def adaptive_traffic_signals(G, traffic_data, t):
    # Adjust green light duration based on traffic conditions at intersections
    for node in G.nodes():
        # Get all edges connected to the node
        connected_edges = G.edges(node)
        total_cars = sum(traffic_data.get(edge, 0) for edge in connected_edges)  # Use get to avoid KeyError
        
        # Example logic: If total cars are above a threshold, increase green light duration
        if total_cars > 5:  # Arbitrary threshold for demonstration
            # Increase green light duration (this is a placeholder for actual signal control logic)
            print(f"{t//6}:{t%6}0|| Node {node}: Increase green light duration due to {total_cars} cars waiting.")
        else:
            ... #print(f"Node {node}: Normal green light duration.")
