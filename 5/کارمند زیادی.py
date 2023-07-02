def my_function():
    numbers = int(input("Enter the number of elements: "))
    dict_name = {}
    duplicate_name = 0
    for _ in range(numbers):
        input_values = input("Enter a key-value pair (separated by a space): ").split(' ')
        key = input_values[0]
        value = input_values[1]
        if key in dict_name:
            dict_name[key].append(value)
        else:
            dict_name[key] = [value]
    print(dict_name)
    
    for key, values in dict_name.items():
        count = len(values)
        print(f"The key '{key}' appears {count} times.")
        if count > duplicate_name:
            duplicate_name = count
    
    print(f"The maximum count of a key is: {duplicate_name}")

my_function()

