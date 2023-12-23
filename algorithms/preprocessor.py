import os
import math
import networkx as nx   # NetworkX is efficient and optimized for handling large graphs.


def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generate_graph(file_name):
    """
    Generates a graph from a TSP file.

    Parameters:
    file_name (str): The name of the TSP file (without the extension).

    Returns:
    networkx.Graph: The generated graph.
    """

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

        for line in file:
            # Process each line of the file and add nodes to the graph
            if line.strip() == "EOF":
                break

            node, x, y = line.split()
            graph.add_node(node, pos=(float(x), float(y)))

    # Connect every node to every other node
    nodes = list(graph.nodes)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node1 = nodes[i]
            node2 = nodes[j]
            if not graph.has_edge(node1, node2):  # Check if edge already exists
                coord1 = graph.nodes[node1]["pos"]
                coord2 = graph.nodes[node2]["pos"]
                distance_value = distance(coord1, coord2)
                graph.add_edge(node1, node2, weight=distance_value)
                graph.add_edge(node2, node1, weight=distance_value)
        del graph.nodes[nodes[i]]["pos"]
        
    return graph
