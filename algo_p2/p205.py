import numpy as np
from typing import Callable
if __name__=="__main__":
    print (-1*np.ones(3, int))
    for n in -1*np.ones(3, int):
        print (n)

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
    pass