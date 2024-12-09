from graph import load_graph, load_nodes, create_graph, plot_graph
from traffic import simulate_traffic, calculate_congestion, identify_top_congested

def main(image_path, graph_file, nodes_file):
    nodes = load_nodes(nodes_file)
    edges = load_graph(graph_file)
    G = create_graph(nodes, edges)

    num_cars = 100 # when not peak hours
    peak_hours = [7, 8, 17, 18]
    traffic_data, high_congestion_duration = simulate_traffic(G, num_cars, peak_hours)

    congestion_info = calculate_congestion(G, traffic_data, high_congestion_duration)

    top_congested = identify_top_congested(congestion_info)

    print("Top 10 Congested Sections:")
    for section in top_congested:
        edge, num_cars, congestion_percentage, duration_high_congestion = section
        print(f"Section: {edge}, Cars: {num_cars}, Congestion: {congestion_percentage:.2f}%, High Congestion Duration: {duration_high_congestion / 6} hours")

    plot_graph(G, image_path, congestion_info, 4)

if __name__ == "__main__":
    main('map.png', 'graph.txt', 'nodes.txt')
