import os
import math
import networkx as nx   # NetworkX is efficient and optimized for handling large graphs.


def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generate_graph(file_name):
    # Construct the file path
    file_path = os.path.join("datasets", file_name + ".tsp")

    # Create an empty graph
    graph = nx.Graph()

    # Read the TSP file and populate the graph
    with open(file_path, "r") as file:
        # Skip lines until "NODE_COORD_SECTION" is found
        for line in file:
            if line.strip() == "NODE_COORD_SECTION":
                break

        # Process the lines after "NODE_COORD_SECTION"
        for line in file:
            # Process each line of the file and add nodes to the graph
            if line.strip() == "EOF":
                break

            node, x, y = line.split()
            graph.add_node(node, pos=(float(x), float(y)))

    # Connect every node to every other node
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            if node1 != node2 and not graph.has_edge(node1, node2):  # Check if edge already exists
                coord1 = graph.nodes[node1]["pos"]
                coord2 = graph.nodes[node2]["pos"]
                distance_value = distance(coord1, coord2)
                graph.add_edge(node1, node2, weight=distance_value)
                graph.add_edge(node2, node1, weight=distance_value)

    return graph
