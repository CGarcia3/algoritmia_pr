import numpy as np
from typing import Callable

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

    print(dist_m)
    current = node_ini
    aux = -1
    while True:
        final_cost = np.Infinity
        for node, cost in enumerate(dist_m[current]):
            if cost > 0 and cost < final_cost and node not in path:
                final_cost = cost
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
    list1=list()
    for node in range(len(dist_m[0])):
        list1 = greedy_tsp(dist_m, node)
        size = len_circuit(list1, dist_m)
        print("Path: {}\nCost: {}".format(list1, size))
        if size < min:
            min = size
            ret = list1
    return ret

def exhaustive_greedy_tsp(dist_m: np.ndarray)-> list:
    return




def init_cd(n:int) -> np.ndarray:
    if n <= 0:
        print("The array should have at least length 1")
        return 

    return -1*np.ones(n, int)

def union(rep_1:int, rep_2:int, p_set:np.ndarray) -> int:
    #Error control
    if (rep_1 < 0 or rep_2 < 0 or p_set is None):
        print("Error in the arguments")
        return -1
    #If rep1 or rep2 are not representatives, we find them
    x = find(rep_1, p_set)
    y = find(rep_2, p_set)
    rank = p_set[y] + p_set[x]
    
    #Check depth of sets to have the optimal union
    if p_set[y] < p_set[x]:
        p_set[x] = y
        p_set[y] = rank
        return y
    else:
        p_set[x] < p_set[y]
        p_set[y] = x
        p_set[x] = rank
        return x


def find(ind:int, p_set:np.ndarray) -> int:

    #Error control
    if p_set is None or ind < 0:
        print("Index < 0 or set is none")
        return -1

    #Find the representative
    z = ind
    while p_set[z] >= 0:
        z = p_set[z]

    #Compress the path
    while p_set[ind] >= 0:
        y = p_set[ind]
        p_set[ind] = z
        ind = y

    return z
     

def cd_2_dict(p_set:np.ndarray) -> dict:
    
    myDict = {}

    #Error control
    if p_set is None:
        print("Array is none")
        return -1

    #Iterate through the set to get the keys
    for indice, value in enumerate(p_set):
        if value < 0:
            myDict[indice] = []
    
    #Iterate to get the values of the set
    for i in range(len(p_set)):
        j = find(i, p_set)
        print("parent:{}\tchild{}".format(j, i))
        myDict[j].append(i)

    return myDict


if __name__=="__main__":

    myDict = {}
    arr = init_cd(9)

    """x = union(2, 1, arr)
    y = union(0, x, arr)
    z = union(y, 3, arr)
    w = union(8, 3, arr)

    a = union(7, 6, arr)
    b = union(4, a, arr)"""

    arr = [2, 2, -4, 1, 7, -1, 7, -3, 3]


    print(arr)

    myDict = cd_2_dict(arr)

    print(myDict)






