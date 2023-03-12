

class DirectedGraph:
    def __init__(self):
        self.__dictionary_predecessor = {}
        self.__dictionary_successor = {}
        self.__dictionary_cost = {}
        self.read_standard_format("graph1.txt")

    def read_standard_format(self, file_name):
        file = open(file_name, "r")
        first_line = file.readline()
        try:
            n, m = first_line.split(" ")
        except Exception:
            return

        lines = file.readlines()
        for line in lines:
            #TODO check for already existing vertexes using is_Vertex
            x, y, cost = line.split(" ")
            self.__dictionary_cost[(x, y)] = cost
            self.__dictionary_successor[x] = y
            self.__dictionary_predecessor[y] = x


