def multiplication(parmeter1):
    result = 3*parmeter1
    print("this is the result for multipliction function",result)
    return result



def multiplication2(parameter2):
    result_from_funtion_one = multiplication(int(input("please enter your number"))) #take input from user and pass it to the calling funtion and stor it 
    final_result= result_from_funtion_one* parameter2
    print("this is the result for multipliction__2",final_result)

multiplication2(int(input("please enter a number")))
