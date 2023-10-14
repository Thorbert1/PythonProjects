def main():
    # Find the closest distance between all pairs of nodes
    # Get user input for source and target nodes
    # Get the distance between the two nodes
    dijkstra()


def get_dist(source_node: int, target_node: int):
    return graph[source_node][target_node]


def dijkstra():
    max_dist = 0
    for node_distances in graph:
        for _ in node_distances:
            if _ > max_dist:
                max_dist = _
    
    for node_distances in graph:
        for i in range(node_distances):
            pass
            



graph = [
    # 0, 1, 2, 3, 4, 5
    [0, 4, 0, 0, 0, 7],
    [4, 0, 3, 8, 0, 0],
    [0, 3, 0, 7, 0, 0],
    [0, 8, 7, 0, 6, 1],
    [0, 0, 0, 6, 0, 5],
    [7, 0, 0, 1, 5, 0],
]

if __name__ == "__main__":
    main()
