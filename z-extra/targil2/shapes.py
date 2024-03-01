import  math

def area_shape():
    chosen = input("Choose shape (1=circle, 2=rectangle, 3=triangle): " )
    if chosen == "1":
        r = float(input())
        s_circle = (math.pi) * r
        return s_circle
    elif chosen == "2":
        a,b = input().split()
        a = float(a)
        b = float(b)
        return (a*b)
    elif chosen == "3":
        a = float(input())
        s_triangle = (math.sqrt(3)*(a*a))/4
        return s_triangle



s = area_shape()
print(s)