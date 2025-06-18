#We use camel case for class names.
class Graphs:

    def __init__(self, directed = False):

        #We use underscores for function names
        #We can as well pass the word 'pass'.
        self.directed = directed

        """
        Graph = {
        A: (B,2), (C,27), (D,89)
        G: (B,2), (C,27), (D,89)
        }
        """
        self.adj_list = dict()

    # This is a dunder method.
    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours} \n"

        return graph_string


    #Used to add a vertice/node to our graph without any neighbours.
    def add_node(self, node):

        #We are checking whether our node is already existent in your graph
        if node not in self.adj_list:

            #Node - key
            #Values in the set - value
            self.adj_list[node] = set()

        else:
            raise ValueError("Node already exists.")

    #Directs specific vertices to the respective neighbours
    def add_edge(self, from_node, to_node, weight = None):
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

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

if __name__ == '__main__':
    Graphs_obj = Graphs(directed= True)

    Graphs_obj.add_edge("A","B",2)
    Graphs_obj.add_edge("A","J",2)
    Graphs_obj.add_edge("A","C",3)
    Graphs_obj.add_edge("A","D",4)
    Graphs_obj.add_edge("B","D")
    Graphs_obj.add_edge("D","C",7)

    print(Graphs_obj)
    print("Breadth First Search: \n")
    print(Graphs_obj.breadth_first_search("A"))

    print("Depth First Search: \n")
    print(Graphs_obj.depth_first_search("A"))
