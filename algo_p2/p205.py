import numpy as np
from typing import Callable

def dist_matrix(n_nodes:int, w_max:int)->np.ndarray:
    x=np.array(np.random.randint(1,w_max, size=(n_nodes,n_nodes)))
    np.fill_diagonal(x, 0, False)
    return x

def greedy_tsp(dist_m: np.ndarray, node_ini=0)-> list:
    return

def len_circuit(circuit: list, dist_m: np.ndarray)-> int:
    return 

def repeated_greedy_tsp(dist_m: np.ndarray)-> list:
    return

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
    myList = []

    #Error control
    if p_set is None:
        print("Array is none")
        return -1

    #Iterate through the set to get the keys
    for indice, value in enumerate(p_set):
        if value < 0:
            myList.append(indice)
            myDict[indice] = myList
    
    #Iterate to get the values of the set
    for i in range(len(p_set)):
        for key in myDict:
            if (p_set[i] == key):
                myList.append(i)
                myDict.update({key:myList})

    return myDict



if __name__=="__main__":

    myDict = {}
    arr = init_cd(8)

    x = union(2, 1, arr)
    y = union(0, x, arr)
    z = union(y, 3, arr)

    a = union(7, 6, arr)
    b = union(4, a, arr)


    print(arr)

    myDict = cd_2_dict(arr)

    print(myDict)






