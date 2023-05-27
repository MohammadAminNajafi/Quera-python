p, d = map(int, input().split())
x = 0

while True:
    x += 1
    y = d * x
    if 0 <= y % p <= p / 2:
        print(y)
        break