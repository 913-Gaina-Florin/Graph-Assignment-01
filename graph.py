

class DirectedGraph:
    def __init__(self):
        self.__dictionary_predecessor = {}
        self.__dictionary_successor = {}
        self.__dictionary_cost = {}
        self.__read_standard_format("graph1.txt")

    def __read_standard_format(self, file_name):
        file = open(file_name, "r")
        first_line = file.readline()
        try:
            n, m = first_line.split(" ")
        except ValueError:
            return

        lines = file.readlines()
        for line in lines:
            pass


