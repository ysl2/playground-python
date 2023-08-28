import numpy as np
cimport numpy as np


cpdef long long example(int x):
    cdef long long y
    cdef long long j
    cdef long long i

    for j in range(x):
        y = 0
        for i in range(x):
            y += i * i
    return y


cpdef void replace_values(np.ndarray[np.double_t, ndim=2] arr, double value):
    cdef double[:, :] arr_view = arr
    cdef int rows = arr_view.shape[0]
    cdef int cols = arr_view.shape[1]

    for r in range(rows):
        for c in range(cols):
            arr_view[r, c] = value
