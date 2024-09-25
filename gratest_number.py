large=int()
print("starting value of large:", large)
first_number =float(input("please enter your first number: "))
second_number=float(input("please enter your second number: "))
third_number=float(input("please enter your third number: "))
if (first_number>second_number) and (first_number>second_number):
    large = first_number
    print("between of these three numbers ",first_number,",",second_number,",",third_number," :"+"the largest number is : ",large,"which is the first number of the list")
elif (second_number>first_number) and (second_number>third_number):
    large = second_number
    print("between of these three numbers ",first_number,",",second_number,",",third_number," :"+"the largest number is : ",large,"which is the second number of the list")

else:
    large = third_number
    print("between of these three numbers ",first_number,",",second_number,",",third_number," :"+"the largest number is : ",large,"which is the third number of the list")



    