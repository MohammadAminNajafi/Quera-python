# walrus = True
# print(walrus)
#
# print(walrus := True)



inputs = list()
while True:
    current = input()
    if current == "quit":
        break
    inputs.append(current)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)