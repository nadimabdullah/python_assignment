def factorial(parameter):
    result =1
    if parameter == 0 or parameter ==1:
        print(parameter,"! is 1")
        print(f'the {parameter}! is 1')
        pass
    else:
        #for i in range(parameter):
           # result = 1*parameter - i #usually when we print i then it start with o,1,2,3 but this code decrease the sequence like 3,2,1
           # result = result* (i+1)
        #return result
        i =1
        while i<=parameter:
              result = result* i
              i=i+1
        return result
    

print(factorial(int(input("please enter a number"))))
