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
    print("8 - Iterate through the set of vertices. ")
    print("9 - Iterate through the set of outbound edges of a vertex. ")
    print("10 - Iterate through the set of inbound edges of a vertex. ")
    print("11 - Make a copy of the graph. ")
    print("12 - Get the number of vertices. ")
    print("13 - Change the cost associated to an edge. ")
    print("14 - Read graph standard format. ")
    print("15 - Read graph special format. ")
    print("16 - Save graph special format. ")


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

            if input_graph.is_vertex(vertex) is True:
                print(f'{vertex} already exists! ')
            else:
                input_graph.add_vertex(vertex)

        elif user_option == "4":
            u = input("Enter the first vertex: ")
            v = input("Enter the second vertex: ")
            cost = input("Enter the cost: ")

            if input_graph.is_edge(u, v) is True:
                print(f'{(u, v)} already exists! ')
            else:
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

        elif user_option == "8":
            print("The set of vertices is: ")
            print(input_graph.get_vertices_iterable())

        elif user_option == "9":
            vertex = input("Enter the vertex: ")
            iterable = input_graph.get_outbound_edges_iterable(vertex)
            print("The outbound edges are: ")

            if iterable is None:
                print(f'{vertex} is not a valid vertex! ')
            elif len(iterable) == 0:
                print(f'{vertex} has no outbound edges! ')
            else:
                print(iterable)

        elif user_option == "10":
            vertex = input("Enter the vertex: ")
            iterable = input_graph.get_inbound_edges_iterable(vertex)
            print("The inbound edges are: ")

            if iterable is None:
                print(f'{vertex} is not a valid vertex! ')
            elif len(iterable) == 0:
                print(f'{vertex} has no inbound edges! ')
            else:
                print(iterable)

        elif user_option == "11":
            copy_object = input_graph.make_copy()
            print("The address of the original graph is: ", input_graph)
            print("The address of the copy is : ", copy_object)

        elif user_option == "12":
            print(input_graph.get_number_vertices())

        elif user_option == "13":
            u = input("Enter the first vertex: ")
            v = input("Enter the second vertex: ")
            cost = input("Enter the cost: ")

            if input_graph.is_edge(u, v) is True:
                input_graph.change_edge_cost(u, v, cost)
            else:
                print(f'The edge {(u, v)} does not exist! ')

        elif user_option == "14":
            file_name = input("Enter the file name: ")
            input_graph.read_standard_format(file_name)

        elif user_option == "15":
            pass

        elif user_option == "16":
            pass


if __name__ == '__main__':
    graph = DirectedGraph("graph1k.txt")
    main_loop(graph)
