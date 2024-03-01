
def calculate_mathematical_expression(num1,act, num2):
    if (act == ":"):
        if num2 == 0:
            result = None
        else:
            result = (num1 / num2)
    elif (act != "*") and (act != "+") and (act != "-"):
        result = None

    else:
        if act == "*":
            result = (num1 * num2)
        if act == "-":
            result = (num1 - num2)
        if act == "+":
            result = (num1 + num2)


    print(result)



def calculate_from_string(string):
    listt = string.split()
    a = float(listt[0])
    b = float(listt[2])
    calculate_mathematical_expression(a,listt[1],b)


calculate_from_string("3 + 2")
calculate_from_string("3 - 2")
calculate_from_string("3 * 2")
calculate_from_string("3 : 2")
calculate_from_string("3 : 0")
calculate_from_string("3 k 2")

#calculate_mathematical_expression(5,":",0)
 #alculate_mathematical_expression(5,"*",0)
#calculate_mathematical_expression(5,"-",1)
#calculate_mathematical_expression(5,":",2)
#calculate_mathematical_expression(5,"*",2.5)
#calculate_mathematical_expression(5,"-",3)
#calculate_mathematical_expression(5,"-",3.5)
#calculate_mathematical_expression(5,"+",2)
#calculate_mathematical_expression(5,"+",5)
