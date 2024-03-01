

def input_list():
    listt = []
    string_from_user = input()
    while string_from_user != '' and string_from_user != "":
        listt.append(float(string_from_user))
        string_from_user = input()
    keeper = 0
    if len(listt) > 0:
        for item in listt:
            sum = keeper + item
            keeper =sum
        listt.append(sum)
    else:
        listt.append(0)

    return listt





def inner_product(vec_1, vec_2):

    if len(vec_1) != len(vec_2):
        return None
    if len(vec_1) == 0:
            return (0)

    contain = 0
    for i in range(len(vec_1)):
        sum = contain + (vec_1[i]*vec_2[i])
        contain = sum

    return sum


def sequence_monotonicity(sequence):
    a = True
    b = True
    c = True
    d = True
    for n in range(1,len(sequence)):
        if sequence[n] > sequence[n-1]:
            c = False
            d = False
        elif sequence[n] == sequence[n-1]:
            b = False
            d = False
        else:
            a = False
            b = False

    boolian_list = [a,b,c,d]
    return boolian_list





def monotonicity_inverse(def_bool):
    boolian_list = [[True,True,False,False],[False,False,True,True]
    ,[True,False,True,False],[False,False,True,False],[True,False,False,False]
    ,[False,False,False,False]]
    souliton_list = [[56.5, 57.5, 63, 84],[7.5, 4, 3.141, 0.111], [2,2,2,2]
        ,[3,2,2,1], [1,2,2,3],[1, 0, -1, 1]]
    for index in range(len(boolian_list)):
        if boolian_list[index] == def_bool:
            return souliton_list[index]
    return None
""" we are able to make sure the function works by the pre function for 6 
different list boolians parameters but not more than that becuase there is no 
list of numbers we can send the pre function for the rest 10 lists of boolians
situations (parameters). (we cannot send the pre function the parametr 'None'
insted list of nums, it will return "ERROR")"""




def primes_for_asafi(n):
    prime_list =[]
    if n==0:
        return None
    else:
        prime_list = [2]
        i = 3
        while len(prime_list) < n:
           for g in range(2,i):
               if i%(g) == 0:
                   i = i +1
                   continue
           prime_list.append(i)
           i = i +1

    return prime_list




def sum_of_vectors(vec_lst):
   LENGH = len(vec_lst[0])
   if len(vec_lst) == []:
        return None
   if LENGH == 0:
       return []
   new_list = []
   for i in range(LENGH):
       holder = 0
       for item in vec_lst:
           sum = holder + item[i]
           holder = sum
       new_list.append(sum)
   return new_list


def num_of_orthogonal(vectors):
    g = 0
    total = 0
    while g < len(vectors)-1:
        for i in range(g+1,len(vectors)):
            if inner_product(vectors[g], vectors[i]) == 0:
               total = total + 1
        g = g +1


    return total




















