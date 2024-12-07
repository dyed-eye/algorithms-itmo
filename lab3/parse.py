import cv2
import numpy as np
import matplotlib.pyplot as plt

def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    return np.array([int(hex_color[i:i + 2], 16) for i in (4, 2, 0)])

def split_line(start, end, segment_length=10):
    line_vector = np.array(end) - np.array(start)
    line_length = np.linalg.norm(line_vector)
    if line_length < segment_length:
        return [start, end]
    num_segments = int(np.ceil(line_length / segment_length))
    segment_vector = line_vector / num_segments
    segments = [start + i * segment_vector for i in range(num_segments + 1)]
    return segments

def parse_graph_image(image_path):
    image = cv2.imread(image_path)
    node_color = hex_to_bgr('#7F0000')
    edge_color = hex_to_bgr('#FF5E55')
    node_mask = cv2.inRange(image, np.array(node_color), np.array(node_color))
    edge_mask = cv2.inRange(image, np.array(edge_color), np.array(edge_color))

    nodes = []
    contours, _ = cv2.findContours(node_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                nodes.append((cX, cY))

    edge_contours, _ = cv2.findContours(edge_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    edges = []
    for contour in edge_contours:
        if cv2.contourArea(contour) > 5:
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            width, height = rect[1]
            start_coord = box[0]
            end_coord = box[1]

            if min(width, height) < 10:
                segments = split_line(start_coord, end_coord, segment_length=10)
                for i in range(len(segments) - 1):
                    nearest_start_node = min(range(len(nodes)), key=lambda j: np.linalg.norm(np.array(nodes[j]) - segments[i]))
                    nearest_end_node = min(range(len(nodes)), key=lambda j: np.linalg.norm(np.array(nodes[j]) - segments[i + 1]))
                    if nearest_start_node != nearest_end_node:
                        edges.append((nearest_start_node, nearest_end_node))
            else:
                nearest_start_node = min(range(len(nodes)), key=lambda j: np.linalg.norm(np.array(nodes[j]) - start_coord))
                nearest_end_node = min(range(len(nodes)), key=lambda j: np.linalg.norm(np.array(nodes[j]) - end_coord))
                if nearest_start_node != nearest_end_node:
                    edges.append((nearest_start_node, nearest_end_node))

    for edge in edges:
        start_node = nodes[edge[0]]
        end_node = nodes[edge[1]]
        cv2.line(image, start_node, end_node, (0, 255, 0), 1)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Detected Rectangles and Edges')
    plt.axis('off')
    plt.show()

    with open('nodes.txt', 'w') as f:
        for node in nodes:
            f.write(f"{node[0]}, {node[1]}\n")

    return nodes, edges
