num = int(input())


def zarb(x):
    while True:
        for i in range(1, x + 1):
            for j in range(1, x + 1):
                print(i * j, end=' ')
            print()
        break


zarb(num)
