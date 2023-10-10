def func(x):
    def inner(x):
        x += 1
        return x
    return inner(x)

if __name__ == "__main__":
    print(func(1))
