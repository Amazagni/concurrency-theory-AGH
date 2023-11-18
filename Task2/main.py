from collections import OrderedDict

from dependency import get_fnf, refactor, get_dependencies, get_independencies
from graph import get_graph_vertices, create_graph, reduce_graph, print_graph


def main(functions, A, w):

    n = len(A)
    used_variables = []

    # wyciagamy wszystkie zmienne wystepujace w naszych funkcjach
    for function in functions:
        used_variables.append(list(OrderedDict.fromkeys([char for char in function if char.isalpha()])))

    dependencies = get_dependencies(used_variables, A, n)
    independencies = get_independencies(dependencies, A, n)

    graph_vertices = get_graph_vertices(A, w, n)

    vertices_count = len(graph_vertices)

    graph = create_graph(A, graph_vertices, dependencies, vertices_count)

    graph = reduce_graph(graph)

    print_graph(graph, graph_vertices, vertices_count)

    fnf = get_fnf(dependencies, A, w, n)

    dependencies = refactor(dependencies, A, n)
    independencies = refactor(independencies, A, n)

    print("D =", dependencies)
    print("I =", independencies)
    print("FNF =", fnf)


functions = ["x := x + 1",
            "y := y + 2z",
            "x := 3x + z",
            "w := w + v",
            "z := y - z",
            "v := x + v"
             ]

A = ["a", "b", "c", "d", "e", "f"]

w = "acdcfbbe"

main(functions, A, w)

