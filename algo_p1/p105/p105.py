from timeit import timeit
import numpy as np
import timeit
from typing import Callable

""" I-A. Midiendo tiempos con %timeit """


def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:
    """
    Function that receives two matrix and perform the multiplication, then returns the result
    """ 
    
    """Check the dimensions to see if they can be multiplied"""
    if(m_1.shape[1]!=m_2.shape[0]):
        return None

    """m_1.rows, m_2.columns"""
    res = np.ndarray((m_1.shape[0], m_2.shape[1])) 

    """Do the multiplication"""
    for i in range(m_1.shape[0]):
        for j in range(m_2.shape[1]):
            sum=0
            for k in range(m_1.shape[1]):
                sum += m_1[i][k]*m_2[k][j] 
            res[i][j] = sum

    return res

""" I-B. Busqueda binaria """


def rec_bb(t: list, f: int, l: int, key: int)-> int:
    """
    Recursive version of binary search, receives the complete list,
    the key to search, and the lower and upper limits of the list
    """
    if f>l:
        return None

    """Get the number that is at the middle of the list"""
    index = int(round((f+l)/2))
    aux=t[index]
    
    """Perform the binary search"""
    if aux==key:
        return index
    elif aux<key:
        return rec_bb(t, index+1, l, key)
    else:
        return rec_bb(t, f, index-1, key)


def bb(t: list, f: int, l: int, key: int)-> int:
    """
    Iterative version of binary search, receives the complete list,
    the key to search, and the lower and upper limits of the list
    """  
    if f>l:
        return None

    """Get the number that is at the middle of the list"""
    index = int(round((f+l)/2))
    
    """Perform the binary search"""
    while t[index]!=key:
        if t[index]<key:
            f=index+1
        elif t[index]>key:
            l=index-1
        if f>l:
            return None
        index = int(round((f+l)/2))
    
    return index

"""I-C. Cuestiones"""

# sin hacer

"""II-A. Min Heaps sobre arrays de Numpy"""

def min_heapify(h: np.ndarray, i: int):
    """
    Function that applies heapify operation to an element of the heap h in position i 
    """
    """Define the child nodes in the array"""
    left_child = 2*i+1
    right_child = 2*i+2 

    """Perform heapify operation"""
    while  left_child < len(h):
        aux = i
        if h[aux] > h[left_child]:
            aux = left_child
        if (right_child) < len(h) and h[aux] > h[right_child]:
            aux = right_child
        if aux > i:
            h[i], h[aux] = h[aux], h[i]
            i = aux
        else:
            return 
            

def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:
    """
    Function that inserts an element in a min heap and 
    returns the heap with the element inserted in its correct position
    """


    """Check if the array is empty"""
    if h == None:
        h = []

    h += [k]
    i = len(h) - 1
    
    """Insert the element in the heap"""
    while i >= 1 and h[(i-1) // 2] > h[i]:
        h[(i-1) // 2], h[i] = h[i], h[(i-1) // 2]
        i = (i-1) // 2

    return h


def create_min_heap(h: np.ndarray):
    """Function that creates a min heap from an array 
    applying heapify in all its elements"""

    """Create an empty array"""
    aux = np.empty(len(h))

    """Create the min heap"""
    for i in range(len(h)):
        min_heapify(h, i)



"""II-B. Colas de prioridad sobre min Heaps"""

def pq_ini():
    """
    Function that initializes a priority queue
    """
    p_queue = []


def pq_insert(h: np.ndarray, k:int) -> np.ndarray:
    """
    Function that inserts an element k in a priority queue
    """

    """Check if the array is empty"""
    if h == None:
        h=[]
    h.append(k)
    return h

def pq_remove(h: np.ndarray) -> np.ndarray:
    """
    Function that removes the element with the least priority
    in a priority queue
    """


    """Check if the array is empty"""
    if h == None:
        return None
    i_min = 0

    """Search the element with the least priority"""
    for i in range(len(h)):
        if h[i] < h[i_min]:
            i_min = i

    elem = h[i_min]
    del h[i_min]

    return elem, h
    
"""II-C. El problema de seleccion"""


def select_min_heap(h: np.ndarray, k:int) -> int:
    """
    Funtion that returns the element of a disordered array that would
    occupy the k position in the ordered version of the array
    """

    """Check if the array is empty"""
    if h is None:
        return -1

    """Change the array to its negative to work with min heap"""
    neg = -1
    aux = neg*np.array(h)
    heap = aux[:k]

    """"""
    create_min_heap(heap)
    for i in range(k, len(h)):
        if aux[i] > heap[0]:
            heap[0] = aux[i]
            min_heapify(heap, 0)
    
    return neg*heap[0]
    
    
