from collections import deque

def bfs(graph, start):
    # Initialize a queue for BFS and add the starting node
    queue = deque([start])
    # A list to track visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")  # Process the current node (e.g., print it)
        
        # Get all adjacent nodes (neighbors) of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue the unvisited neighbors
                visited.add(neighbor)   # Mark them as visited

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
