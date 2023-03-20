from graph import DirectedGraph


def print_options():
    print("x - Exit. ")
    print("1 - Get in degree for a vertex.")
    print("2 - Get out degree for a vertex. ")
    print("3 - Add a vertex. ")
    print("4 - Add an edge. ")
    print("5 - Check edge existence. ")
    print("6 - Get a cost associated to an edge. ")
    print("7 - Print the graph to the screen. ")


def main_loop(input_graph: DirectedGraph):
    while True:
        print_options()

        user_option = input(">")

        if user_option == "x":
            return
        elif user_option == "1":
            vertex = input("Enter the vertex: ")
            in_degree = input_graph.get_in_degree(vertex)

            if in_degree is None:
                print("The vertex does not exist")
                continue
            print("The in degree is: ", in_degree)

        elif user_option == "2":
            vertex = input("Enter the vertex: ")
            out_degree = input_graph.get_out_degree(vertex)

            if out_degree is None:
                print("The vertex does not exist")
            print("The out degree is: ", out_degree)

        elif user_option == "3":
            vertex = input("Enter the vertex: ")
            input_graph.add_vertex(vertex)

        elif user_option == "4":
            u = input("Enter the first vertex: ")
            v = input("Enter the second vertex: ")
            cost = input("Enter the cost: ")
            input_graph.add_edge(u, v, int(cost))

        elif user_option == "5":
            u = input("Enter the first vertex: ")
            v = input("Enter the second vertex: ")
            print(input_graph.is_edge(u, v))

        elif user_option == "6":
            u = input("Enter the first vertex: ")
            v = input("Enter the second vertex: ")
            cost = input_graph.get_cost(u, v)

            if cost is None:
                print("The edge does not exist! ")
                continue
            print("The cost is: ", cost)

        elif user_option == "7":
            input_graph.print_graphh()


if __name__ == '__main__':
    graph = DirectedGraph("graph1.txt")
    main_loop(graph)
