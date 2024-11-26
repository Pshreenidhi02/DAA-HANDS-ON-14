def bellman_ford(graph, start):

    nodes = set()
    for u, v, _ in graph:
        nodes.add(u)
        nodes.add(v)
    
    distances = {node: float('inf') for node in nodes}
    predecessors = {node: None for node in nodes}
    distances[start] = 0


    for _ in range(len(nodes) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u

  
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            return distances, predecessors, True  # Negative cycle detected

    return distances, predecessors, False

def reconstruct_path(predecessors, start, end):
   
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    return path[::-1] if path and path[-1] == start else []

# Test cases from diagrams
test_cases = [
    {
        "graph": [
            ('s', 't', 6), ('s', 'y', 7), 
            ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), 
            ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2),
            ('z', 's', 7), ('z', 'x', 6),
            ('x', 'z', -2)
        ],
        "start": 's',
        "description": "Graph (a)"
    },
    {
        "graph": [
            ('s', 't', 6), ('s', 'y', 7),
            ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
            ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2),
            ('z', 's', 7), ('z', 'x', 6),
            ('x', 'z', -2)
        ],
        "start": 't',
        "description": "Graph (b)"
    },
    {
        "graph": [
            ('s', 't', 6), ('s', 'y', 7),
            ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
            ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2),
            ('z', 's', 7), ('z', 'x', 6),
            ('x', 'z', -2)
        ],
        "start": 'y',
        "description": "Graph (c)"
    },
]


print("Bellman-Ford Algorithm Test Cases\n" + "=" * 40)
for i, case in enumerate(test_cases, 1):
    graph = case["graph"]
    start = case["start"]
    description = case["description"]

    print(f"\nTest Case {i}: {description}")
    print(f"Graph: {graph}")
    print(f"Start Node: {start}")

    distances, predecessors, has_negative_cycle = bellman_ford(graph, start)

    if has_negative_cycle:
        print("Result: Negative-weight cycle detected.")
    else:
        print(f"Shortest Distances: {distances}")
        print(f"Predecessors: {predecessors}")
        # Print paths to all nodes
        for node in distances:
            path = reconstruct_path(predecessors, start, node)
            print(f"Shortest Path to {node}: {path if path else 'No path exists'}")
