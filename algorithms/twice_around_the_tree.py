import networkx as nx

def solve(graph):
    """
    Solves the Travelling Salesperson Problem using the Twice Around the Tree algorithm.

    Parameters:
    graph (networkx.Graph): The input graph.

    Returns:
    tuple: A tuple containing the Hamiltonian circuit and it's total distance/weight.
    """

    # Create a minimum spanning tree
    mst = nx.minimum_spanning_tree(graph)

    # Create a Eulerian circuit
    eulerian_circuit = nx.MultiGraph(mst)   # Copies the graph
    eulerian_circuit.add_edges_from(mst.edges())   # Doubles the edges by adding them once more

    # Create a Hamiltonian circuit by removing repeated vertices from the Eulerian circuit
    hamiltonian_circuit = list(nx.eulerian_circuit(eulerian_circuit))

    # Calculate the total weight of the Hamiltonian circuit
    total_weight = sum(graph[u][v]['weight'] for u, v in hamiltonian_circuit)

    return hamiltonian_circuit, total_weight