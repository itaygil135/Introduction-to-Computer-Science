import math

def quadratic_equation(a,b,c):
    before_sqr = (b*b) - (4*a*c)
    if before_sqr < 0:
        sol1,sol2 = None,None

    elif before_sqr == 0:
        sol1 = ((-b)/ (2*a))
        sol2 = None

    else:
        sqrt = math.sqrt(before_sqr)
        sol1 = ((-b + sqrt) / (2*a))
        sol2 = ((-b - sqrt)/(2*a))


    return (sol1,sol2)


def quadratic_equation_user_input():
    listt = input("Insert coefficients a, b, and c: ").split()
    listt = [float(listt[0]),float(listt[1]),float(listt[2])]
    if listt[0] == 0:
        print("The parameter 'a' may not equal 0 ")
    else:
        x,y = quadratic_equation(listt[0],listt[1],listt[2])
        if x == None:
            print("The equation has no solutions ")
        elif y == None:
            print("The equation has 1 solution:" ,x)
        else:
            print("The equation has 2 solutions:", x ,"and",y)





quadratic_equation_user_input()