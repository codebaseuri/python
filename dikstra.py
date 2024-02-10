import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))


def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    predecessors = {node: None for node in graph.nodes}
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def shortest_path(predecessors, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = predecessors[target]
    return path


def main():
    graph = Graph()
    graph.add_node('0')
    graph.add_node('1')
    graph.add_node('2')
    graph.add_node('3')
    graph.add_node('4')
    graph.add_node('5')

    graph.add_edge('0', '1', 5)
    graph.add_edge('0', '2', 1)
    graph.add_edge('1', '2', 2)
    graph.add_edge('1', '3', 3)
    graph.add_edge('1', '4', 20)
    graph.add_edge('2', '1', 3)
    graph.add_edge('2', '4', 12)
    graph.add_edge('3', '5', 6)
    graph.add_edge('3', '2', 3)
    graph.add_edge('3', '4', 2)
    graph.add_edge('4', '5', 1)

    source_node = '0'
    distances, predecessors = dijkstra(graph, source_node) # finds the fastest path to all node from node 0
    print("Shortest distances from node", source_node + ":")
    for node, distance in distances.items():
        print(node, ":", distance)

    target_node = '5'
    shortest_path_nodes = shortest_path(predecessors, target_node)
    print("Shortest path to", target_node + ":", shortest_path_nodes)
    #print(distances)
    #print(predecessors)

if __name__ == "__main__":
    main()