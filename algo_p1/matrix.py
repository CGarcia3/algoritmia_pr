from timeit import timeit
import numpy as np
import timeit

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

    #m  = np.random.uniform(0., 1., (10, 10))
    #m = np.arange(4).reshape((2,2))
    #print(m)
    #x = matrix_multiplication(m, m)
    #print(x)
    
    