import numpy as np
from typing import Callable
import itertools as it

def dist_matrix(n_nodes:int, w_max:int)->np.ndarray:
    arr = np.ndarray(shape=(n_nodes,n_nodes), dtype=int)
    for i in range(n_nodes):
        for j in range(n_nodes):
            if i!=j:
                x=np.random.randint(1, w_max)
                arr[i][j] = x
                arr[j][i] = x
            else:
                arr[i][j] = 0

    return arr

def greedy_tsp(dist_m: np.ndarray, node_ini=0)-> list:
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

def len_circuit(circuit: list, dist_m: np.ndarray)-> int:
    sum = 0
    for index in range(1, len(circuit)):
        sum += dist_m[circuit[index-1]][circuit[index]]
    return sum

def repeated_greedy_tsp(dist_m: np.ndarray)-> list:
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

def exhaustive_greedy_tsp(dist_m: np.ndarray)-> list:
    circ = list()    
    ret = list()
    l = it.permutations(range(len(dist_m[0])))
    min = np.Infinity
    for i in l:
        x = list(i)
        x.append(x[0])

        cost = len_circuit(x, dist_m)
        print(x, cost)
        if cost < min:
            min = cost
            ret = x
    print(ret, min)
    return ret



if __name__=="__main__":
    x=dist_matrix(4, 10)
    z=exhaustive_greedy_tsp(x)