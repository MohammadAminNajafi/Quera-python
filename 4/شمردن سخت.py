def count_ones(n):
    binary = bin(n)[2:]
    ones_count = binary.count('1')
    return ones_count


n = int(input())
ones_count = count_ones(n)
print(ones_count)
