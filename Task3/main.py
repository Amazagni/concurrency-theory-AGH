import copy
import threading

from graphviz import Digraph


def main(N):
    A = copy.deepcopy(N)
    n = len(N)

    moves = []
    # standard way
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            moves.append("A" + str(k + 1) + str(i + 1))
            for j in range(k, n + 1):
                x = factor * A[k][j]
                moves.append("B" + str(k + 1) + str(j + 1) + str(i + 1))
                A[i][j] -= x
                moves.append("C" + str(k + 1) + str(j + 1) + str(i + 1))

    dependencies = get_dependencies(n)
    foaty = get_foaty(n)

    gauss(N, n)

    for i in range(n):
        for j in range(n, i - 1, -1):
            A[i][j] = A[i][j] / A[i][i]
            N[i][j] = N[i][j] / N[i][i]

    print("Poprawna postać:")
    for i in range(n):
        print(A[i])
    print()
    print("Postać po algorytmie współbieżnym:")
    for i in range(n):
        print(N[i])

    print()
    print("Czynności:")
    print(moves)
    print()
    print("D:")
    print(dependencies)
    print()
    print("Foaty:")
    print(foaty)
    print_graph(moves, dependencies)


def count_a(N, k, i, factor):
    factor[i] = N[i][k] / N[k][k]


def count_b(N, k, i, j, subs, factor):
    subs[i][j] = N[k][j] * factor


def count_c(N, i, j, sub):
    N[i][j] -= sub


def get_dependencies(n):
    D = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(i, n + 2):
                D.append(("A" + str(i) + str(j), "B" + str(i) + str(k) + str(j)))
                D.append(("B" + str(i) + str(k) + str(j), "C" + str(i) + str(k) + str(j)))
                if (k == n or k == n + 1) and i != n:
                    if j == n:
                        D.append(("C" + str(i) + str(k) + str(j), "C" + str(i + 1) + str(k) + str(j)))
                    else:
                        D.append(("C" + str(i) + str(k) + str(j), "B" + str(i + 1) + str(k) + str(j + 1)))

                if (j == k == n + 1 and i != n + 1):
                    D.append(("C" + str(i) + str(k) + str(j), "C" + str(i + 1) + str(k) + str(j)))
            if i != 1:
                D.append(("C" + str(i - 1) + str(i) + str(i), "A" + str(i) + str(j)))
                D.append(("C" + str(i - 1) + str(i) + str(j), "A" + str(i) + str(j)))
    return D


def get_foaty(n):
    Foaty = []
    for i in range(1, n):
        tmp = []
        for j in range(i + 1, n + 1):
            tmp.append("A" + str(i) + str(j))
        Foaty.append(tmp)
        tmp = []
        for j in range(i, n + 1):
            for k in range(i + 1, n + 2):
                tmp.append("B" + str(i) + str(j) + str(k))
        Foaty.append(tmp)
        tmp = []
        for j in range(i, n + 1):
            for k in range(i + 1, n + 2):
                tmp.append("C" + str(i) + str(j) + str(k))
        Foaty.append(tmp)
    return Foaty


def print_graph(moves, D):
    digraph = Digraph()

    for move in moves:
        digraph.node(move)
    for d in D:
        digraph.edge(d[0], d[1])

    # Zapisanie grafu do pliku i wyswietlenie go
    digraph.render('visualization/graph', format='png', cleanup=True)
    digraph.view()


def gauss(N, n):
    for k in range(n - 1):
        factor = [0 for i in range(n)]
        a_s = []
        for i in range(k + 1, n):
            thread = threading.Thread(target=count_a, args=(N, k, i, factor))
            thread.start()
            a_s.append(thread)

        for thread in a_s:
            thread.join()

        subs = [[0 for i in range(n + 1)] for j in range(n)]
        b_s = []
        for i in range(k + 1, n):
            for j in range(k, n + 1):
                thread = threading.Thread(target=count_b, args=(N, k, i, j, subs, factor[i]))
                thread.start()
                b_s.append(thread)

        for thread in b_s:
            thread.join()

        c_s = []
        for i in range(k + 1, n):
            for j in range(k, n + 1):
                thread = threading.Thread(target=count_c, args=(N, i, j, subs[i][j]))
                thread.start()
                c_s.append(thread)

        for thread in c_s:
            thread.join()


N = [[2, 1, 3, 6],
     [4, 3, 8, 15],
     [6, 5, 16, 27]]

# N = [[2, 1, 3, 1],
#      [4, 3, 8, 3],
#      [6, 5, 16, 12],
#      [8, 12, 23, 12]]

main(N)