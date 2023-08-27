from example import example
import time

x = 9999
# Call the 'add' function
start = time.time()
result = example(x)
end = time.time()
print("Result:", result)


def example1(x):
    y = None
    for _ in range(x):
        y = sum(i * i for i in range(x))
    return y


start1 = time.time()
result = example1(x)
end1 = time.time()
print("Result:", result)

print("Time C:", f'{(end - start):.8f}')
print("Time P:", f'{(end1 - start1):.8f}')

# Result: 333183354999
# Result: 333183354999
# Time C: 0.06645274
# Time P: 6.54512691
