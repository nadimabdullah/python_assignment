def add_unique_items_in_a_list(parameter):
    unique_items =[]
    for i in range(parameter):
        unique_items.append(i)
    return unique_items
#print(add_unique_items_in_a_list(int(input("plese inset the number"))))

def del_list(func): #recive a function by the parameter 
    result= func(int(input("enter the number"))) # received funtion by parameter is save as a variable and pass arguments to the fuction as input
    print(result)

del_list(add_unique_items_in_a_list) # calling another funtion as a arguments



