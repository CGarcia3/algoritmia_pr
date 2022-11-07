import numpy as np
from typing import Callable
import itertools as it


def dist_matrix(n_nodes: int, w_max: int) -> np.ndarray:
    """
    It will create the distance matrix with
    random values. The matrix is symmetric
    Parameters: int, int (The number of nodes and the max random number)
    Returns: np.ndarray (Array of two dimensions)
    """

    arr = np.ndarray(shape=(n_nodes, n_nodes), dtype=int)
    for i in range(n_nodes):
        for j in range(n_nodes):
            if i != j:
                x = np.random.randint(1, w_max)
                arr[i][j] = x
                arr[j][i] = x
            else:
                arr[i][j] = 0

    return arr


def greedy_tsp(dist_m: np.ndarray, node_ini=0) -> list:
    """
    It will iterate through the distance matrix and
    will check the cost of each node to get the one
    that costs the less and is not in the path
    Parameters: np.ndarray, int (The distance matrix and the initial node)
    Returns: list (The path with the less cost)
    """

    path = list()
    path.append(node_ini)

    current = node_ini
    aux = -1
    while True:
        min_cost = np.Infinity
        for node, cost in enumerate(dist_m[current]):
            if cost > 0 and cost < min_cost and node not in path:
                min_cost = cost
                aux = node

        current = aux
        path.append(current)

        if len(path) == len(dist_m[node_ini]):
            path.append(node_ini)
            break
    return path


def len_circuit(circuit: list, dist_m: np.ndarray) -> int:
    """
    Get the total cost of the circuit
    Parameters: list, np.ndarray (The path and the distance matrix)
    Returns: int (The cost of the path)
    """

    sum = 0
    for index in range(1, len(circuit)):
        sum += dist_m[circuit[index-1]][circuit[index]]
    return sum


def repeated_greedy_tsp(dist_m: np.ndarray) -> list:
    """
    It will perform greedy_tsp but starting with all the nodes
    Parameters: np.ndarray (The distance matrix)
    Returns: list (The path with less cost)
    """

    min = np.Infinity
    ret = list()
    list1 = list()
    for node in range(len(dist_m[0])):
        list1 = greedy_tsp(dist_m, node)
        size = len_circuit(list1, dist_m)
        print("Path: {}\nCost: {}".format(list1, size))
        if size < min:
            min = size
            ret = list1
    return ret


def exhaustive_tsp(dist_m: np.ndarray) -> list:
    """
    It will traverse all the paths possible in
    the distance matrix and get the path with
    the least cost among all
    Parameters: np.ndarray(The distance matrix)
    Returns: list (The path with the least cost)
    """

    circ = list()
    ret = list()
    li = it.permutations(range(len(dist_m[0])))
    min = np.Infinity
    for i in li:
        x = list(i)
        x.append(x[0])

        cost = len_circuit(x, dist_m)
        if cost < min:
            min = cost
            ret = x

    return ret


def init_cd(n: int) -> np.ndarray:
    """
    Initializes a disjoint set
    Parameters: int (Number of nodes the set will have)
    Returns: np.ndarray (The array with all values -1)
    """
    if n <= 0:
        print("The array should have at least length 1")
        return

    return -1*np.ones(n, int)


def union(rep_1: int, rep_2: int, p_set: np.ndarray) -> int:
    """
    It will perform a union between two disjoint sets
    taking into account their rank
    Parameters: int, int, np.ndarray (Two indices to join and the entire set)
    Returns: int (The representative after the union of the sets)
    """

    # Error control
    if (rep_1 < 0 or rep_2 < 0 or p_set is None):
        print("Error in the arguments")
        return -1
    # If rep1 or rep2 are not representatives, we find them
    x = find(rep_1, p_set)
    y = find(rep_2, p_set)
    rank = p_set[y] + p_set[x]

    # Check depth of sets to have the optimal union
    if p_set[y] < p_set[x]:
        p_set[x] = y
        p_set[y] = rank
        return y
    else:
        p_set[x] < p_set[y]
        p_set[y] = x
        p_set[x] = rank
        return x


def find(ind: int, p_set: np.ndarray) -> int:
    """
    It will find the representative of an index and
    will apply path compression on the set
    Parameters: int, np.ndarray (the index and the entire set)
    Returns: int (The representative of the arg node)
    """

    # Error control
    if p_set is None or ind < 0:
        print("Index < 0 or set is none")
        return -1

    # Find the representative
    z = ind
    while p_set[z] >= 0:
        z = p_set[z]

    # Compress the path
    while p_set[ind] >= 0:
        y = p_set[ind]
        p_set[ind] = z
        ind = y

    return z


def cd_2_dict(p_set: np.ndarray) -> dict:
    """
    Will transform the set of disjoint sets into a dictionary
    Parameters: np.ndarray (The entire set)
    Returns: dict (The dictionary with the disjoint sets)
    """

    myDict = {}

    # Error control
    if p_set is None:
        print("Array is none")
        return -1

    # Iterate through the set to get the keys
    for indice, value in enumerate(p_set):
        if value < 0:
            myDict[indice] = []

    # Iterate to get the values of the set
    for i in range(len(p_set)):
        j = find(i, p_set)
        myDict[j].append(i)

    return myDict


def ccs(n: int, li: list) -> dict:
    """
    Will iterate through a list of tuples and will do t
    union of the tuples. After all the list ios iterated,
    a dictionary with the disjoint sets will be created
    Parameters: int, list (The number of nodes and the list)
    Returns: dict (The dictionary with the disjoint sets)
    """

    k = 0
    myDict = {}

    # Initialize the CD
    arr = init_cd(n)

    # Iterate through the list, find the representatives
    # of each node of the tuple and check if they belong
    # to the same set, if not , unify them
    for a in li:
        i = find(a[0], arr)
        j = find(a[1], arr)
        if (i != j):
            k = union(a[0], a[1], arr)

    myDict = cd_2_dict(arr)

    return myDict


if __name__ == "__main__":

    myDict = {}
    myList = [(0, 2), (1, 3), (2, 3), (2, 4), (3, 4), (5, 6), (5, 7), (6, 8)]
    myDict = ccs(9, myList)

    print(myDict)
