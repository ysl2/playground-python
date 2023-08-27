import ctypes
import time

# Load the shared library
lib = ctypes.CDLL('./example.so')  # Use './example.dll' on Windows

# Define the argument and return types for the 'add' function
lib.example.argtypes = (ctypes.c_int,)
lib.example.restype = ctypes.c_longlong

x = 9999
# Call the 'add' function
start = time.time()
result = lib.example(x)
end = time.time()
print("Result:", result)


def example(x):
    y = None
    for _ in range(x):
        y = sum(i * i for i in range(x))
    return y


start1 = time.time()
result = example(x)
end1 = time.time()
print("Result:", result)

print("Time C:", f'{(end - start):.8f}')
print("Time P:", f'{(end1 - start1):.8f}')
