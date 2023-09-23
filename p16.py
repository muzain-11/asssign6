
my_list = []
while True:
    element = input("Enter an element (press 'q' to stop): ")
    if element.lower() == 'q':
        break
    my_list.append(element)


search_element = input("Enter an element to search and delete: ")

if search_element in my_list:
    my_list.remove(search_element)

for element in my_list:
    print(element)
