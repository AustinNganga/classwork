import heapq  # Needed for Dijkstra's algorithm

# We use camel case for class names.
class Graphs:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""
        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours} \n"
        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists.")

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

    def breadth_first_search(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def depth_first_search(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)
                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def shortest_path(self, start_node):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0

        priority_queue = [(0, start_node)]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbour in self.obtain_neighbours(current_node):
                if isinstance(neighbour, tuple):
                    neighbour_node, weight = neighbour
                else:
                    neighbour_node, weight = neighbour, 1  # default weight

                distance = current_distance + weight

                if distance < distances[neighbour_node]:
                    distances[neighbour_node] = distance
                    heapq.heappush(priority_queue, (distance, neighbour_node))

        return distances


if __name__ == '__main__':
    Graphs_obj = Graphs(directed=True)

    Graphs_obj.add_edge("A", "B", 2)
    Graphs_obj.add_edge("A", "J", 2)
    Graphs_obj.add_edge("A", "C", 3)
    Graphs_obj.add_edge("A", "D", 4)
    Graphs_obj.add_edge("B", "D", 1)
    Graphs_obj.add_edge("D", "C", 7)

    print("Graph structure:\n")
    print(Graphs_obj)

    print("Breadth First Search: \n")
    print(Graphs_obj.breadth_first_search("A"))

    print("Depth First Search: \n")
    print(Graphs_obj.depth_first_search("A"))

    print("Shortest Path First (Dijkstra) from node A:\n")
    shortest_paths = Graphs_obj.shortest_path("A")
    for node, distance in shortest_paths.items():
        print(f"Distance from A to {node} = {distance}")
