import networkx as nx
import networkx as nx

def solve(graph):
    """"
    Solves the Travelling Salesperson Problem using the Christofides algorithm.

    Args:
        graph (NetworkX Graph): The input graph representing the cities and distances.

    Returns:
        tuple: A tuple containing the Hamiltonian circuit and it's total distance/weight.

    """
    # Create a minimum spanning tree (MST) of the input graph
    mst = nx.minimum_spanning_tree(graph)

    # Create a set of vertices with odd degree from the MST
    odd_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]

    # Create a minimum-weight perfect matching on the subgraph induced by the odd vertices
    subgraph = graph.subgraph(odd_vertices)
    perfect_matching = nx.min_weight_matching(subgraph)

    # Combine the MST and the perfect matching to form a multigraph
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(perfect_matching)

    # Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))

    # Remove duplicate vertices from the Eulerian circuit
    visited = set()
    hamiltonian_circuit = [v for u, v in eulerian_circuit if v not in visited and not visited.add(v)]

    # Calculate the total distance of the Hamiltonian circuit
    total_distance = sum(graph[u][v]['weight'] for u, v in zip(hamiltonian_circuit, hamiltonian_circuit[1:]))

    return hamiltonian_circuit, total_distance