def find_duplicates(input_list):
    new_list_without_duplicates = []
    
    for item in input_list:
       if item not in new_list_without_duplicates:
        new_list_without_duplicates.append(item)
    return new_list_without_duplicates



list_items =[1,2,2,10,4,5,8,9,4,10]
result1=find_duplicates(list_items)
print('this is the list with duplicates',list_items)
print('this is the unique list',result1)