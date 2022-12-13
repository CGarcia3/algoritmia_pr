import numpy as np
import itertools
import time

from typing import List, Tuple, Dict, Callable, Iterable, Union


def split(t: np.ndarray) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    Splits a given array into two arrays each containing
    the smaller and bigger values in regard to the first element
    of the array.

    **Params:** array (The array to split)

    **Return:** Tuple(array, int, array) (The two arrays that result
    after the split, and the value used to split the array)
    """

    if (t is None):
        #print("Array is empty")
        return None

    p = t[0]
    arr_left = [u for u in t if u < p]
    arr_right = [u for u in t if u > p]

    return (arr_left, p, arr_right)


def qsel(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Recursive function that finds the k-th element of the
    given array if it was ordered.

    **Params:** array, int (The array containing the values,
    and the k index)

    **Return:** int (element in the k-th position)
    """

    if (k < 0 or t is None or k > len(t)-1):
        #print("K is smaller than 0 or array is empty")
        return None

    if len(t) == 1:
        return t[0]

    arr_left, p, arr_right = split(t)
    m = len(arr_left)

    if k == m:
        return p
    elif k < m:
        return qsel(arr_left, k)
    elif k > m:
        return qsel(arr_right, k-m-1)


def qsel_nr(t: np.ndarray, k: int) -> Union[int, None]:
    """
    Implementation of the qsel function without the tail
    recursion.

    **Params:** array, int (The array containing the values,
    and the k index)

    **Return:** int (element in the k-th position)
    """
    p = None
    m = -1
    while k != len(t): 
        if (k < 0 or t is None or k > len(t)-1):
            #print("K is smaller than 0 or array is empty")
            return None

        if len(t) == 1:
            return t[0]
            
        arr_left, p, arr_right = split(t)
        m = len(arr_left)

        if k == m:
            break
        
        if k < m:
            t = arr_left
            
        elif k > m:
            t = arr_right
            k = k-m-1

    return p


def split_pivot(t: np.ndarray, mid: int) -> Tuple[np.ndarray, int, np.ndarray]:
    """
    Function that splits the array into two othe arrays
    containig the values greater and lower than t[mid].

    **Params:** array, int (The array containing the values,
    and the mid index to be used as a pivot)

    **Return:** (array, int, array) (tuple containing the
    two splitted arrays and the pivot)
    """
    
    if (t is None or mid < 0):
        #print("Array is empty or non valid mid value")
        return None

    arr_left = [u for u in t if u < mid]
    arr_right = [u for u in t if u > mid]

    return (arr_left, mid, arr_right)


def pivot5(t: np.ndarray) -> int:
    #Hay que llamar a qsel5 cuando tengas el array de medians para que se haga en qsel5
    if t is None or len(t) == 0:
        #print("Array is empty")
        return None
    
    if len(t) < 5:
        aux = sorted(t)
        return aux[int(len(t)/2)]

    i = 0
    med_arr = []
    
    
    while i < len(t):
        res = len(t) - i
        if res >= 5:
            arr5 = t[i:i+4] 
            #piv5 = np.median(arr5)
            aux = sorted(arr5)
            piv5 = aux[int(len(aux)/2)]
            med_arr.append(piv5) 
            i += 5
        else:
            arr5 = t[i:]
            aux = sorted(arr5)
            piv5 = aux[int(len(arr5)/2)]
            med_arr.append(piv5)
            break

    pivot = qsel5_nr(med_arr, int(len(med_arr)/2))

    return pivot

def qsel5_nr(t: np.ndarray, k: int) -> Union[int, None]:

    if (t is None):
        #print("Array is empty or non valid mid value")
        return None
    if  k < 0 or k >= len(t):
        #print("Non valid k ", t, k)
        return None


    if len(t) == 1:
        return t[0]
    
    m = -1
    while k != len(t):
        p = pivot5(t)
        
        if p is None:
            return None
        p = int(p)

        arr_left, p, arr_right = split_pivot(t, p)
        m = len(arr_left)

        if k == m:
            break
        if k < m:
            t = arr_left
        elif k > m:
            t = arr_right
            k = k-m-1
       
    return p

def qsort_5(t: np.ndarray) -> np.ndarray:
    aux = np.zeros(len(t), dtype=int)
    for elem in t:
        index = qsel5_nr(t, elem)
        aux[index] = elem
    return aux

def edit_distance(str1: str, str2: str) -> int:    
    dist = np.zeros((len(str1)+1, len(str2)+1), dtype=int)
    dist[0, 1:] = range(1, len(str2)+1)
    dist[1:, 0] = range(1, len(str1)+1)
    
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            dist[i, j] = dist[i-1, j-1] if str1[i-1] == str2[j-1] else 1 + min(dist[i-1, j-1], dist[i-1, j], dist[i, j-1])

    return dist[-1,-1]

def max_subsequence_length(str_1: str, str_2: str) -> int:    
    lth = np.zeros((len(str_1)+1, len(str_2)+1), dtype=int)
    
    for i in range(1, len(str_1)+1):
        for j in range(1, len(str_2)+1):
            lth[i, j] = 1 + lth[i-1, j-1] if str_1[i-1] == str_2[j-1] else max(lth[i-1, j], lth[i, j-1])
    print(lth)
    return lth[-1, -1]

def max_ind(indList:List) -> int:
    max_val = max(indList)
    max_ind = indList.index(max_val)
    return max_ind

def max_common_subsequence(str_1: str, str_2: str) -> str:
    lth = np.zeros((len(str_1)+1, len(str_2)+1), dtype=int)
    move_matrix = np.empty((len(str_1)+1, len(str_2)+1), dtype=str)
    
    for i in range(1, len(str_1)+1):
        for j in range(1, len(str_2)+1):
            if str_1[i-1] == str_2[j-1]:
                lth[i, j] = 1 + lth[i-1, j-1]
                move_matrix[i,j] = 'D'
            else:
                lth[i,j] = max(lth[i-1, j], lth[i, j-1])
                ind = max_ind((lth[i-1, j], lth[i, j-1]))
                move_matrix[i,j] = 'U' if ind else 'L'
    print(move_matrix)
    print(lth)

    sc = ""
    while move_matrix[i, j] != '':
        if move_matrix[i, j] == 'D':
            i, j = i-1, j-1
            sc = str_1[i] + sc
        elif move_matrix[i, j] == 'U':
            j = j-1
        elif move_matrix[i, j] == 'L':
            i = i-1 
        print(i, j)
    return sc

def min_mult_matrix(l_dims: List[int]) -> int:
    mult = np.ones((len(l_dims),len(l_dims))) * np.inf
    mult[0, 0] = 0

    """Multiply a matrix for itself = 0"""
    for i in range(len(l_dims)):
        mult[i][i] = 0

    """Matrix dimension A is l_dims[i-1] x l_dims[i]"""
    for i in range(1, len(l_dims)):
        for j in range(1, len(l_dims)):
            for k in range(i, j):
                cost = mult[i][k] + mult[k + 1][j] + l_dims[i - 1] * l_dims[k] * l_dims[j]
                print(cost)
                if cost < mult[i][j]:
                    mult[i][j] = cost

    print(mult)
    return mult[1][len(l_dims) - 1]
            

if __name__ == "__main__":
    """arr = np.random.permutation(1000)
    key = int(np.random.rand(1)*1000)
    e = qsel(arr, key)
    f = qsel5_nr(arr, key)
    if e != key:
        print("Error qsel. ", e, key)
    if f != key:
        print("Error qsel_nr. ", f, key)"""

    """while True:
        arr = np.random.permutation(10)
        key = int(np.random.rand(1)*10)
        f = qsel5_nr(arr, key)
        if f != key:
            print("Error qsel_nr. ", f, key, arr)
            break
        #time.sleep(0.1)
        print(f, key)"""

    """while True:
        arr = np.random.permutation(10)
        print(arr)
        for key in range(10):
            f = qsel5_nr(arr, key)
            print(f, key)
            if f != key:
                print("Error qsel_nr. ", f, key)
                time.sleep(10)
"""

    """arr = np.random.permutation(100)
    print(arr)
    ord = qsort_5(arr)
    print(ord)
    for x, y in enumerate(ord):
        if x!=y:
            print("ERROR")
            time.sleep(10)
    print("OK")"""

    y = "qwertyluiolp"
    x = "helolo"

    dist = edit_distance(x, y)
    print (f'Edit distance:{dist}')
