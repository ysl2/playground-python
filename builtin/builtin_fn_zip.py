def transpose_2d(arr):
    return list(zip(*arr))


def test_transpose_2d():
    arr = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print(transpose_2d(arr))


if __name__ == '__main__':
    test_transpose_2d()
