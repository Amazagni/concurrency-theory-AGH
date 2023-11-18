from graphviz import Digraph

from vertex import Vertex


def get_graph_vertices(A, w, n):
    letters_count = [0 for i in range(n)]
    graph_vertices = []

    # utworzenie tabeli zawierajacej wszystkie wierzcholki naszego grafu,
    # wierzcholek sklada sie z odpowiedniej litery oraz numeru wystapienia danej litery
    # numer sluzy nam do odróźnienia dwoch identycznych wierzcholkow
    for letter in w:
        index = A.index(letter)
        graph_vertices.append(Vertex(letter, letters_count[index]))
        letters_count[index] += 1

    return graph_vertices


def create_graph(A, graph_vertices, dependencies, vertices_count):
    graph = [[0 for _i in range(vertices_count)] for _j in range(vertices_count)]

    # utworzenie grafu w postaci macierzowej (najprosciej na niej wykonac algorytm redukcji)
    for i in range(vertices_count):
        index = A.index(graph_vertices[i].letter)
        for j in range(i + 1, vertices_count):
            if graph_vertices[j].letter in dependencies[index]:
                graph[i][j] = 1

    return graph


def reduce_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                if graph[i][j] == 1 and graph[j][k] == 1 and graph[i][k] == 1:
                    graph[i][k] = 0
    return graph


def print_graph(graph, graph_vertices, vertices_count):
    digraph = Digraph()

    # zapisanie wierzcholkow i krawedzi a nastepnie wypisanie grafu przy pomocy graphviz
    for vertex in graph_vertices:
        digraph.node(vertex.__repr__())

    for i in range(vertices_count):
        for j in range(vertices_count):
            if graph[i][j]:
                digraph.edge(graph_vertices[i].__repr__(), graph_vertices[j].__repr__())


    # Zapisanie grafu do pliku i wyswietlenie go
    digraph.render('visualization/graph', format='png', cleanup=True)
    digraph.view()