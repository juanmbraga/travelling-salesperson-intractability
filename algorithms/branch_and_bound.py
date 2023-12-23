import numpy as np

def solve(graph):
    # Initialize variables
    n = graph.number_of_nodes()
    visited = [False] * n
    path = []
    min_cost = np.inf

    # Helper function to calculate the lower bound cost
    def calculate_lower_bound(curr_node, visited):
        nonlocal graph, n
        lower_bound = 0

        # Calculate the cost of the edges from the current node to the unvisited nodes
        for i in range(n):
            if not visited[i]:
                min_edge_cost = min(graph[curr_node][j]['weight'] for j in range(n) if not visited[j])
                lower_bound += min_edge_cost

        return lower_bound

    # Helper function to perform the branch and bound search
    def branch_and_bound(curr_node, visited, curr_cost, path):
        nonlocal graph, n, min_cost

        # Base case: All nodes have been visited
        if len(path) == n:
            # Add the cost of returning to the starting node
            curr_cost += graph[curr_node][path[0]]['weight']

            # Update the minimum cost and path if necessary
            if curr_cost < min_cost:
                min_cost = curr_cost
                path.append(path[0])

            return

        # Calculate the lower bound cost
        lower_bound = calculate_lower_bound(curr_node, visited)

        # Prune the branch if the lower bound exceeds the current minimum cost
        if lower_bound >= min_cost:
            return

        # Explore the unvisited neighbors
        for neighbor in graph.neighbors(curr_node):
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                branch_and_bound(neighbor, visited, curr_cost + graph[curr_node][neighbor]['weight'], path)
                path.pop()
                visited[neighbor] = False

    # Start the branch and bound search from each node
    for start_node in range(n):
        visited[start_node] = True
        path.append(start_node)
        branch_and_bound(start_node, visited, 0, path)
        path.pop()
        visited[start_node] = False

    return min_cost, path
