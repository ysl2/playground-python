import pudb; pudb.set_trace()  # HACK: Songli.Yu: ""


def main():
    x = 1
    for _ in range(10):
        x += x


if __name__ == '__main__':
    main()
