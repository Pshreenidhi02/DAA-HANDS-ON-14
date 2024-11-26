import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest path in a weighted graph.
    Parameters:
        graph (dict): Adjacency list (node -> [(neighbor, weight)]).
        start (str): Starting node.
    Returns:
        distances (dict): Shortest distance from the start node to each node.
        previous (dict): Tracks the parent of each node in the shortest path tree.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

def reconstruct_path(previous, start, end):
    """
    Reconstructs the shortest path from start to end using the parent dictionary.
    Parameters:
        previous (dict): Parent dictionary (node -> parent node).
        start (str): Starting node.
        end (str): Destination node.
    Returns:
        list: The shortest path from start to end as a list of nodes.
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1] if path and path[-1] == start else []

# Graphs for testing
test_cases = [
    {
        "graph": {
            's': [('t', 10), ('y', 5)],
            't': [('x', 1), ('y', 2)],
            'y': [('t', 3), ('x', 9), ('z', 2)],
            'x': [('z', 4)],
            'z': [('s', 7), ('x', 6)]
        },
        "start": 's',
        "end": 'z',
        "description": "Standard graph with multiple paths"
    },
    {
        "graph": {
            'a': [('b', 1), ('c', 4)],
            'b': [('c', 2), ('d', 6)],
            'c': [('d', 3)],
            'd': []
        },
        "start": 'a',
        "end": 'd',
        "description": "Simple graph with unique shortest path"
    },
    {
        "graph": {
            'x': [('y', 2)],
            'y': [('z', 3)],
            'z': [('x', 1)]
        },
        "start": 'x',
        "end": 'z',
        "description": "Cyclic graph"
    },
    {
        "graph": {
            'p': [('q', 10)],
            'q': [('r', 5)],
            'r': [],
            's': []
        },
        "start": 'p',
        "end": 'r',
        "description": "Disconnected graph with no path between some nodes"
    },
    {
        "graph": {
            'm': [],
            'n': []
        },
        "start": 'm',
        "end": 'n',
        "description": "Empty graph or no connections"
    }
]

# Run all test cases
print("Dijkstra's Algorithm Test Cases\n" + "="*30)
for i, case in enumerate(test_cases, 1):
    graph = case["graph"]
    start = case["start"]
    end = case["end"]
    description = case["description"]

    print(f"\nTest Case {i}: {description}")
    print(f"Graph: {graph}")
    print(f"Start Node: {start}, End Node: {end}")

    distances, previous = dijkstra(graph, start)
    path = reconstruct_path(previous, start, end)

    print(f"Shortest Distances: {distances}")
    print(f"Shortest Path from {start} to {end}: {path if path else 'No path exists'}")
