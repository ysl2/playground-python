import example
import time
import numpy as np
import copy

x = 9999
# Call the 'add' function
start = time.time()
result = example.example(x)
end = time.time()
print('Result:', result)


def example1(x):
    y = None
    for _ in range(x):
        y = sum(i * i for i in range(x))
    return y


start1 = time.time()
result = example1(x)
end1 = time.time()
print('Result:', result)

print('Time C:', f'{(end - start):.8f}')
print('Time P:', f'{(end1 - start1):.8f}')

m = 5.0
arr = np.zeros([x, x])
arr1 = copy.deepcopy(arr)

start = time.time()
example.replace_values(arr, m)
end = time.time()
print('Result:', arr[0, 0])


def replace_values1(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i, j] = m


start1 = time.time()
replace_values1(arr1)
end1 = time.time()
print('Result:', arr[0, 0])

print('Time C:', f'{(end - start):.8f}')
print('Time P:', f'{(end1 - start1):.8f}')

# Result: 333183354999
# Result: 333183354999
# Time C: 0.04707837
# Time P: 6.43233371
# Result: 5.0
# Result: 5.0
# Time C: 0.44542933
# Time P: 12.59173203
