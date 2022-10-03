from timeit import timeit
import numpy as np
import timeit
from typing import Callable

""" I-A. Midiendo tiempos con %timeit """

"""
Function that receives two matrix and perform the multiplication
"""
def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:
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
"""
if __name__=="__main__":
    l_timings = []
    
    for i in range(11):
        dim = 10+i
        m = np.random.uniform(0., 1., (dim, dim))
        timings = %timeit -o -n 10 -r 5 -q matrix_multiplication(m, m)
        l_timings.append([dim, timings.best])

    print(l_timings)
"""

""" I-B. Busqueda binaria """

"""
Recursive version of binary search
"""
def rec_bb(t: list, f: int, l: int, key: int)-> int:
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


"""
Iterative version of binary search
"""  
def bb(t: list, f: int, l: int, key: int)-> int:
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

"""
def script2():
    l_times = []
    for i, size in enumerate(range(5, 15)):
        t = list(range(2**i * size))
        key = ...
        timings = %timeit -n 100 -r 10 -o -q ...(t, 0, len(t) - 1, key)
        l_times.append([len(t), timings.best])
        times = np.array(l_times)
    print(l_times)
"""    

"""I-C. Cuestiones"""


def fit_func_2_times(timings: np.ndarray, func_2_fit: Callable):
    """Ajusta linealmente los valores de la funcion func_2_fit a
    los tiempos en timings.
    Esto es, calculamos valores a, b para que la funcion a*f(dim) + b
    se ajuste a los tiempos medidos.
    """
    """if len(timings.shape) == 1:
        timings = timings.reshape(-1, 1)
    values = func_2_fit(timings[ :, 0]).reshape(-1, 1)
    
    #normalizar timings
    times = timings[ : , 1] / timings[0, 1]
    
    #ajustar a los valores en times un modelo lineal sobre los valores en values
    lr_m = LinearRegression()
    lr_m.fit(values, times)
    return lr_m.predict(values)"""
    pass

def func_2_fit(n):

    # IDEA: Devolver tuplas de valores de un plot que tenga en x la dimension (n), y
    # en y el tiempo que tarda en realizar la multiplicacion
    
    # IDEA2: Devolver valores de tiempo
    pass


"""II-A. Min Heaps sobre arrays de Numpy"""

"""
Function that applies heapify operation to an element in position i 
"""
def min_heapify(h: np.ndarray, i: int):
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
            

"""
Function that inserts an element in a min heap and 
returns the heap with the element inserted
"""
def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:

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


"""Function that creates a min heap from an array"""
def create_min_heap(h: np.ndarray):
    """Create an empty array"""
    aux = np.empty(len(h))

    """Create the min heap"""
    for i in range(len(h)):
        aux[i] = h[i]
        min_heapify(aux, i)

    h = aux



"""II-B. Colas de prioridad sobre min Heaps"""

"""
Function that initializes a priority queue
"""
def pq_ini():
    p_queue = []

"""
Function that inserts an element k in a priority queue
"""
def pq_insert(h: np.ndarray, k:int) -> np.ndarray:
    """Check if the array is empty"""
    if h == None:
        h=[]
    h.append(k)
    return h

"""
Function that removes the element with the least priority
in a priority queue
"""
def pq_remove(h: np.ndarray) -> np.ndarray:
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

"""
Function that selects the element k in a disordered array
"""
def select_min_heap(h: np.ndarray, k:int) -> int:
    """Check if the array is empty"""
    if h == None:
        return -1

    """Create a min heap and get the element with the least priority"""
    create_min_heap(h)
    elem, h = pq_remove(h) 

    return elem
