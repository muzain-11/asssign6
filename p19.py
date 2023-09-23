
original_list = [1, 'apple', 2.5, 'banana', 3, 'cherry', 4.7]


int_list = []
str_list = []
float_list = []


for item in original_list:
    
    if isinstance(item, int):
        int_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)


print("Integers:", int_list)
print("Strings:", str_list)
print("Floats:", float_list)
