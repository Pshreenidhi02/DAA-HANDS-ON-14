def floyd_warshall(graph):
  

    nodes = list(graph.keys())
    dist = {u: {v: graph[u][v] for v in nodes} for u in nodes}

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def print_matrix(matrix):
    """
    Helper function to print the adjacency matrix nicely.
    """
    nodes = list(matrix.keys())
    print("   ", " ".join(f"{node}" for node in nodes))
    for i in nodes:
        row = [f"{matrix[i][j]:3}" if matrix[i][j] != float('inf') else "inf" for j in nodes]
        print(f"{i}: ", " ".join(row))


nodes = [1, 2, 3, 4]
inf = float('inf')

graph = {
    1: {1: 0, 2: inf, 3: inf, 4: inf},
    2: {1: inf, 2: 0, 3: 1, 4: 1},
    3: {1: inf, 2: 1, 3: 0, 4: inf},
    4: {1: 1, 2: inf, 3: inf, 4: 0},
}


print("Initial Adjacency Matrix (T^(0)):")
print_matrix(graph)

# Run Floyd-Warshall and print the results after each iteration
distances = floyd_warshall(graph)

print("\nShortest Path Matrix after Floyd-Warshall (T^(4)):")
print_matrix(distances)
