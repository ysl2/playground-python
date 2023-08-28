import example
import time
import numpy as np
import copy
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def _timeit(*args, **kwargs):
        print('Func:', fn.__name__)
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('Time:', f'{(end - start):.8f}')
        return result
    return _timeit


X = 9999


def test():
    timeit(example.example)(X)

    @timeit
    def example1(x):
        y = None
        for _ in range(x):
            y = sum(i * i for i in range(x))
        return y

    example1(X)


def test1():
    m = 5.0
    arr = np.zeros([X, X])
    arr1 = copy.deepcopy(arr)

    timeit(example.replace_values)(arr, m)

    @timeit
    def replace_values1(arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i, j] = m

    replace_values1(arr1)


if __name__ == '__main__':
    test()

# Result: 333183354999
# Result: 333183354999
# Time C: 0.04707837
# Time P: 6.43233371
# Result: 5.0
# Result: 5.0
# Time C: 0.44542933
# Time P: 12.59173203
