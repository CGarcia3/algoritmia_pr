import matplotlib.pyplot as plt
from timeit import timeit
from ..import p105

def plot1():
    l_timings = []
    for i in range(11):
        dim = 10+i
        h = list(np.random.permutation(dim))
        timings = %timeit -o -n 10 -r 5 -q create_min_heap(h)
        l_timings.append([dim, timings.best])

    print(l_timings)