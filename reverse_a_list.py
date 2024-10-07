def reverse_list(input_list):
    new_list =[]
    length_of_input_list= len(input_list)
    i = 1
    while i <= (length_of_input_list):
        new_list.append(input_list[length_of_input_list - i])
        i+=1
    return new_list


input_list =[10,20,30,40,50]
reversed_list = reverse_list(input_list)
print(f'the list provided by the user is {input_list}')
print (f'the reversed list is {reversed_list}')