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
        print("Array is empty")
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

    if (k < 0 or t is None):
        print("K is smaller than 0 or array is empty")
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

    m = -1
    while k != len(t): 
        if (k < 0 or t is None):
            print("K is smaller than 0 or array is empty")
            return None

        if len(t) == 1:
            return t[0]
            
        arr_left, p, arr_right = split(t)
        m = len(arr_left)
        #print("This is k: "+ str(k))
        #print("This is p: "+str(p))

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
        print("Array is empty or non valid mid value")
        return None

    arr_left = [u for u in t if u < mid]
    arr_right = [u for u in t if u > mid]

    return (arr_left, mid, arr_right)


def pivot5(t: np.ndarray) -> int:
    #Hay que llamar a qsel5 cuando tengas el array de medians para que se haga en qsel5
    if t is None or len(t) == 0:
        print("Array is empty")
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
        print("Array is empty or non valid mid value")
        return None
    if  k < 0 or k >= len(t):
        print("Non valid k ", t, k)
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
    """else:
        p = pivot5(t)
        if p is None:
            return None
        p = int(p)

        arr_left, p, arr_right = split_pivot(t, p)
        m = len(arr_left)

        if k == m:
            ret = p
        elif k < m:
            ret = qsel5_nr(arr_left, k)
        elif k > m:
            ret = qsel5_nr(arr_right, k-m-1)

    return ret"""

def qsort5_5(t: np.ndarray) -> np.ndarray:
    pass


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

    while True:
        arr = np.random.permutation(100)
        print(arr)
        for key in range(100):
            f = qsel_nr(arr, key)
            print(f, key)
            if f != key:
                print("Error qsel_nr. ", f, key)
                time.sleep(10)

"""
[7 1 9 6 5 3 0 4 2 8]
[4 6 8 2 5 7 9 0 3 1]
[9 1 0 3 5 7 6 4 8 2]
[4 3 7 1 6 9 8 0 5 2]
"""