def find_max_unique_letters(names):
    max_unique_letters = max(names, key=lambda x: len(set(x)) if x.isalpha() else 0)
    return len(set(max_unique_letters))

list_of_names = [input() for _ in range(int(input()))]
max_unique = find_max_unique_letters(list_of_names)
print(max_unique)
