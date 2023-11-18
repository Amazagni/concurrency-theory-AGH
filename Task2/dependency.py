def get_dependencies(used_variables, A, n):
    dependencies = [[] for i in range(n)]

    # znajdujemy wszystkie zależności dla danych zmiennych
    for i in range(n):
        variable_to_check = used_variables[i][0]
        for j in range(n):
            if variable_to_check in used_variables[j]:
                dependencies[i].append(A[j])

    # sprawdzamy czy wszystkie zależności dzialaja "w obie strony"
    for i in range(n):
        for dependency in dependencies[i]:
            if A[i] not in dependencies[A.index(dependency)]:
                dependencies[A.index(dependency)].append(A[i])

    return dependencies


def get_independencies(dependencies, A, n):
    independencies = [[] for i in range(n)]

    # szukamy liter ktore nie naleza do danych zaleznosci i je zwracamy
    for i in range(n):
        for letter in A:
            if letter not in dependencies[i]:
                independencies[i].append(letter)

    return independencies

def get_fnf(dependencies, A, w, n,):
    stacks = ["" for _ in range(n)]

    # tworzymy stacki reprezentujace tabele zgodnie z zaleceniami podczas laboratoriow
    for letter in w[::-1]:
        index = A.index(letter)
        stacks[index] = letter + stacks[index]
        for dependency in dependencies[index]:
            if letter != dependency:
                dependency_index = A.index(dependency)
                stacks[dependency_index] = "*" + stacks[dependency_index]

    fnf = []
    take_letters = True

    # dopoki jest cos na ktoryms ze stackow to naprzemiennie sciagamy litery oraz gwiazdki
    while stacks:
        current_letters = []
        for i in range(len(stacks)):
            if take_letters and stacks[i][0] != "*":
                current_letters.append(stacks[i][0])
                stacks[i] = stacks[i][1:]
            if not take_letters and stacks[i][0] == "*":
                stacks[i] = stacks[i][1:]
        stacks = [stack for stack in stacks if stack != ""]

        # gwiazdy zapisujemy w naszej tablicy fnf
        if current_letters:
            fnf.append(current_letters)
        take_letters = not take_letters
    return fnf


def refactor(curr_list, A, n):
    new_list = []
    # sprowadzamy listy do postaci zgodnej z ta w poleceniu
    for i in range(n):
        for letter in curr_list[i]:
            new_list.append([A[i], letter])

    return new_list
