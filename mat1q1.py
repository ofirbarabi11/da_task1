def my_func(x1,x2,x3):
    if type(x1)== str or type(x2)== str or type(x3) == str:
        return "None"
    elif type(x1)!= float or type(x2)!= float or type(x3)!= float:
        return "Error: parameters should be float"
    if (x1+x2+x3)== 0:
        return "Not a number – denominator equals zero"
    return float((x2+x3)*x3)
print(my_func(1.,2.,3.))