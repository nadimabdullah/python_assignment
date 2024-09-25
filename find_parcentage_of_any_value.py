"""
 This program is find out the parcentage of attandence of a student and if 
 the percentage is below then 75% the student doesn't allow to sit in the 
 exam
"""
import math

#define function for calculate the percentage
def find_percentage():
    result = math.floor((total_class_attended/total_class_in_a_semister)*100 )# formula for find percentage is value/total_value * 100 %
    return result

#take user input
minimum_parcentage_must_be_attend =int(input("please enter the minimum percentage of attendance"))
total_class_in_a_semister = int(input("please enter the total number of class in a semister : "))
total_class_attended = int(input("please enter the total number of class has been attended by the student : "))

if find_percentage() >= minimum_parcentage_must_be_attend:
   
   print("Congrats!you are allowed to sit to the exam because the percentage of you attend is ",find_percentage(),"% which is grater than the minimum percentage(",minimum_parcentage_must_be_attend,"%)") 
else:
    
    print("sorry you are not allowed to sit to the exam because the percentage of you attend is ",find_percentage(),"% which is lower than the minimum percentage(",minimum_parcentage_must_be_attend,"%)")



