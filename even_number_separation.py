def even_number_separation(input_list):
    even_number_list =[]
    odd_number_list = []
    length_of_input_list = len(input_list)
    for i in range (length_of_input_list):

        if input_list[i] % 2 ==0:
            even_number_list.append(input_list[i])
        else:
            odd_number_list.append(input_list[i])

    return even_number_list,odd_number_list

input_list =[1,2,4,5,8,9,375,41,45,12,36]
result_even,result_odd =even_number_separation(input_list)
print(result_even,result_odd)
