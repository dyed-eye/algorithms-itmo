from graph import load_graph, load_nodes, create_graph, plot_graph
from traffic import simulate_traffic, calculate_congestion, identify_top_congested


def main(image_path, graph_file, nodes_file):
    nodes = load_nodes(nodes_file)
    edges = load_graph(graph_file)
    G = create_graph(nodes, edges)

    # Simulate traffic
    num_cars = 100  # Total number of cars
    peak_hours = [7, 8, 17, 18]  # Example peak hours
    traffic_data = simulate_traffic(G, num_cars, peak_hours)

    # Calculate congestion
    congestion_info = calculate_congestion(G, traffic_data)

    # Identify top congested sections
    top_congested = identify_top_congested(congestion_info)

    # Display results
    print("Top 10 Congested Sections:")
    for section in top_congested:
        print(f"Section: {section[0]}, Cars: {section[1]}, Congestion: {section[2]:.2f}%")

    # Plot the graph
    plot_graph(G, image_path, congestion_info, 4)

if __name__ == "__main__":
    main('map.png', 'graph.txt', 'nodes.txt')
