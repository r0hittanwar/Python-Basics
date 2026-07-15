# write a recursive function to print all elements in a list.

list = ["Apple", "Banana", "Mango", "Litchi"]

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list(list)