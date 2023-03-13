import copy


class DirectedGraph:
    def __init__(self):
        self.__dictionary_predecessor = {}
        self.__dictionary_successor = {}
        self.__dictionary_cost = {}
        self.read_standard_format("graph1.txt")

    def print_graphh(self):
        # test function
        for key in self.__dictionary_cost.keys():
            print(key, self.__dictionary_cost[key])

    def is_vertex(self, vertex):
        if vertex in self.__dictionary_predecessor.keys():
            return True
        if vertex in self.__dictionary_successor.keys():
            return True
        return False

    def get_in_degree(self, vertex):
        if not self.is_vertex(vertex):
            return None
        return len(self.__dictionary_predecessor[vertex])

    def get_number_vertices(self):
        return len(self.__dictionary_successor)

    def get_number_edges(self):
        return len(self.__dictionary_cost)

    def get_out_degree(self, vertex):
        if not self.is_vertex(vertex):
            return None
        return len(self.__dictionary_successor[vertex])

    def is_edge(self, u, v):
        if (u, v) in self.__dictionary_cost.keys():
            return True
        return False

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

    def make_copy(self):
        return copy.deepcopy(self)

    def read_standard_format(self, file_name):
        file = open(file_name, "r")
        first_line = file.readline()
        try:
            n, m = first_line.split(" ")
        except Exception:
            return

        lines = file.readlines()
        for line in lines:
            # TODO check for already existing vertexes using is_Vertex
            x, y, cost = line.split(" ")
            self.add_vertex(int(x))
            self.add_vertex(int(y))
            self.add_edge(int(x), int(y), int(cost))
