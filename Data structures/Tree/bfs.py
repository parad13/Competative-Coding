# BFS/BFT(Breadth first Search/Traversal)/Level wise traversal

def bfs(graph, start):
    # Initialize a list to use as the queue and add the starting node
    queue = [start]
    # A list to track visited nodes
    visited = set([start])
    
    while queue:
        # Remove the first node in the queue (FIFO)
        node = queue.pop(0)
        print(node, end=" ")  # Process the current node (e.g., print it)
        
        # Get all adjacent nodes (neighbors) of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Add the unvisited neighbors to the queue
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

