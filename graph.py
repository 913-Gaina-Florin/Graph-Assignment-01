import copy
from random import randint


class DirectedGraph:
    def __init__(self):
        self.__dictionary_predecessor = {}
        self.__dictionary_successor = {}
        self.__dictionary_cost = {}

    def print_graphh(self):
        # test function
        for key in self.__dictionary_cost.keys():
            print(key, self.__dictionary_cost[key])

    def __clear_memory(self):
        self.__dictionary_predecessor.clear()
        self.__dictionary_successor.clear()
        self.__dictionary_cost.clear()

    def is_vertex(self, vertex):
        if vertex in self.__dictionary_predecessor.keys():
            return True
        if vertex in self.__dictionary_successor.keys():
            return True
        return False

    def get_cost(self, u, v):
        if not self.is_edge(u, v):
            return None
        return self.__dictionary_cost[(u, v)]

    def get_in_degree(self, vertex):
        if not self.is_vertex(vertex):
            return None
        return len(self.__dictionary_predecessor[vertex])

    def get_number_vertices(self):
        return len(self.__dictionary_successor)

    def get_number_edges(self):
        return len(self.__dictionary_cost)

    def get_vertices_iterable(self):
        vertices_array = []
        for key in self.__dictionary_predecessor.keys():
            vertices_array.append(key)
        return vertices_array

    def change_edge_cost(self, u, v, cost):
        if self.is_edge(u, v) is False:
            return
        self.__dictionary_cost[(u, v)] = cost

    def get_outbound_edges_iterable(self, vertex):
        edges_array = []
        if not self.is_vertex(vertex):
            return None
        for adj_vertex in self.__dictionary_successor[vertex]:
            edges_array.append((vertex, adj_vertex))
        return edges_array

    def get_inbound_edges_iterable(self, vertex):
        edges_array = []
        if not self.is_vertex(vertex):
            return None
        for adj_vertex in self.__dictionary_predecessor[vertex]:
            edges_array.append((adj_vertex, vertex))
        return edges_array

    def get_out_degree(self, vertex):
        if not self.is_vertex(vertex):
            return None
        return len(self.__dictionary_successor[vertex])

    def is_edge(self, u, v):
        if not self.is_vertex(u) or not self.is_vertex(v):
            return False

        found = False
        for vertex_predecessor in self.__dictionary_predecessor[v]:
            if vertex_predecessor == u:
                found = True
                break

        if found is False:
            return False

        found = False
        for vertex_successor in self.__dictionary_successor[u]:
            if vertex_successor == v:
                found = True
                break

        if found is False:
            return False

        return True

    def add_vertex(self, vertex):
        if not self.is_vertex(vertex):
            self.__dictionary_predecessor[vertex] = []
            self.__dictionary_successor[vertex] = []

    def add_edge(self, u, v, cost):
        if not self.is_vertex(u) or not self.is_vertex(v):
            return

        if not self.is_edge(u, v):
            self.__dictionary_predecessor[v].append(u)
            self.__dictionary_successor[u].append(v)
            self.__dictionary_cost[(u, v)] = cost

    def delete_vertex(self, vertex):
        if not self.is_vertex(vertex):
            return False

        for predecessor in self.__dictionary_predecessor[vertex]:
            self.__dictionary_successor[predecessor].remove(vertex)
            del self.__dictionary_cost[(predecessor, vertex)]

        for successor in self.__dictionary_successor[vertex]:
            self.__dictionary_predecessor[successor].remove(vertex)
            del self.__dictionary_cost[(vertex, successor)]

        del self.__dictionary_predecessor[vertex]
        del self.__dictionary_successor[vertex]
        return True

    def delete_edge(self, u, v):
        if not self.is_edge(u, v):
            return False

        self.__dictionary_successor[u].remove(v)
        self.__dictionary_predecessor[v].remove(u)
        del self.__dictionary_cost[(u, v)]
        return True

    def write_special_format(self, file_name):
        file = open(file_name, "w+")

        all_nodes = list(self.__dictionary_successor.keys())
        all_nodes.sort()

        for vertex in all_nodes:
            if len(self.__dictionary_successor[vertex]) == 0 and len(self.__dictionary_predecessor[vertex]) == 0:
                file.write(f'{vertex} -1')
                file.write("\n")

            for successor in self.__dictionary_successor[vertex]:
                file.write(f'{vertex} {successor} {self.__dictionary_cost[(vertex, successor)]}')
                file.write("\n")

        file.close()

    def read_special_format(self, file_name):
        self.__clear_memory()

        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            args = line.strip('\n').split(" ")
            if len(args) == 2:
                self.add_vertex(args[0])
            elif len(args) == 3:
                self.add_vertex(args[0])
                self.add_vertex(args[1])
                self.add_edge(args[0], args[1], args[2])

        file.close()

    def make_copy(self):
        return copy.deepcopy(self)

    def read_standard_format(self, file_name):
        self.__clear_memory()

        file = open(file_name, "r")
        first_line = file.readline()
        try:
            n, m = first_line.strip('\n').split(" ")
        except Exception:
            print("Error reading the file. ")
            return

        for vertex in range(int(n)):
            self.add_vertex(str(vertex))

        lines = file.readlines()
        for line in lines:
            x, y, cost = line.strip('\n').split(" ")
            self.add_vertex(x)
            self.add_vertex(y)
            self.add_edge(x, y, cost)

    def generate_random_graph(self, nr_vertices, nr_edges):
        self.__clear_memory()

        if nr_edges > nr_vertices * nr_vertices:
            nr_edges = nr_vertices * nr_vertices

        counter = 0
        while counter < nr_edges:
            u = randint(0, nr_vertices - 1)
            v = randint(0, nr_vertices - 1)
            cost = randint(0, 250)

            if not self.is_edge(u, v):
                self.add_vertex(u)
                self.add_vertex(v)
                self.add_edge(u, v, cost)
                counter += 1
