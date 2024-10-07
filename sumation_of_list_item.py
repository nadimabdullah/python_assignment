"""
Write a Python function that takes a list of numbers as input and returns the sum of all the elements in the list.
input_numbers = [1, 2, 3, 4, 5]
Sum: 15

"""
def sumation_of_input_list(input_number):
    sum =0
    items = input_number
    for i in range(len(items)):
        sum = sum+ items[i]
    print(sum)

input_number_list = [1,2,3,4,5,6]
sumation_of_input_list(input_number_list)