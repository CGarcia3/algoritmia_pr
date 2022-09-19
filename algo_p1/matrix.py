from timeit import timeit
import numpy as np
import timeit

""" I-A. Midiendo tiempos con %timeit """

def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:
    if(m_1.shape[1]!=m_2.shape[0]):
        return None

    res = np.ndarray((m_1.shape[0], m_2.shape[1])) #m_1.rows, m_2.columns
    for i in range(m_1.shape[0]):
        for j in range(m_2.shape[1]):
            sum=0
            for k in range(m_1.shape[1]):
                sum += m_1[i][k]*m_2[k][j] 
            res[i][j] = sum

    return res

if __name__=="__main__":
    l_timings = []
    
    for i in range(11):
        dim = 10+i
        m = np.random.uniform(0., 1., (dim, dim))
        timings = %timeit -o -n 10 -r 5 -q matrix_multiplication(m, m)
        l_timings.append([dim, timings.best])

    print(l_timings)


""" I-B. Busqueda binaria """

def rec_bb(t: list, f: int, l: int, key: int)-> int:
    if f>l:
        return None

    index = int(round((f+l)/2))
    aux=t[index]
    
    if aux==key:
        return index
    elif aux<key:
        return rec_bb(t, index+1, l, key)
    else:
        return rec_bb(t, f, index-1, key)

        
def bb(t: list, f: int, l: int, key: int)-> int:
    if f>l:
        return None

    index = int(round((f+l)/2))
    
    while t[index]!=key:
        if t[index]<key:
            f=index+1
        elif t[index]>key:
            l=index-1
        if f>l:
            return None
        index = int(round((f+l)/2))
    
    return index


def script2():
    l_times = []
    for i, size in enumerate(range(5, 15)):
        t = list(range(2**i * size))
        key = ...
        timings = %timeit -n 100 -r 10 -o -q ...(t, 0, len(t) - 1, key)
        l_times.append([len(t), timings.best])
        times = np.array(l_times)
    print(l_times)
    

"""I-C. Cuestiones"""
import Callable
from sklearn.linear_model import LinearRegression

    def fit_func_2_times(timings: np.ndarray, func_2_fit: Callable):
        """Ajusta linealmente los valores de la funcion func_2_fit a
        los tiempos en timings.
        Esto es, calculamos valores a, b para que la funcion a*f(dim) + b
        se ajuste a los tiempos medidos.
        """
        if len(timings.shape) == 1:
            timings = timings.reshape(-1, 1)
        values = func_2_fit(timings[ :, 0]).reshape(-1, 1)
        
        #normalizar timings
        times = timings[ : , 1] / timings[0, 1]
        
        #ajustar a los valores en times un modelo lineal sobre los valores en values
        lr_m = LinearRegression()
        lr_m.fit(values, times)
        return lr_m.predict(values)

def func_2_fit(n):

    # IDEA: Devolver tuplas de valores de un plot que tenga en x la dimension (n), y
    # en y el tiempo que tarda en realizar la multiplicacion
    
    # IDEA2: Devolver valores de tiempo
    return ...   