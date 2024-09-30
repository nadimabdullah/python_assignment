
"""
def about_return():
    a = int(input("please input a number"))
    b = int(input("please input a number"))
    c = int(input("please input a number"))
    d = int(input("please input a number"))
    return a,c,b,d
a,b,c,d=about_return()
print(a)
"""
def sq_cube(a):
    sq = a**2
    cube =a**3
    return sq,cube
result1,r2 =sq_cube(int(input("please enter a number")))
print(r2)