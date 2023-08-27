cpdef long long example(int x):
    cdef long long y
    cdef long long j
    cdef long long i

    for j in range(x):
        y = 0
        for i in range(x):
            y += i * i
    return y
