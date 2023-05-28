def comb(n, r):
    result1 = 1
    result2 = 1
    result3 = 1
    if n > 1:
        for i in range(2, n + 1):
            result1 *= i
            if i == n:
                if r == 0 or r == n:
                    return 1
                if r > n:
                    return 0
                if r > 1:
                    for j in range(2, r + 1):
                        result2 *= j
                        if j == r:
                            for z in range(2, n - r + 1):
                                result3 *= z
                                if z == n - r:
                                    finaly = result1 / (result2 * result3)
                                    return int(finaly)
                        if n - r <= 2 and j == r:
                            finaly = result1 / (result2 * result3)
                            return int(finaly)
                else:
                    return n
    else:
        return 1


print(comb(10, 8))




