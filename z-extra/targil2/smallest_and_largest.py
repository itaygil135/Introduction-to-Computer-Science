

def largest_and_smallest(a,b,c):
    min_val = a
    max_val = a
    if b > max_val:
         max_val = b
    if c > max_val:
      max_val = c
    if b < min_val:
         min_val = b
    if c < min_val:
        min_val = c

    return (min_val,max_val)




def check_largest_and_smallest():
    min_val, max_val = largest_and_smallest(17,1,6)
    if min_val != 1 or max_val != 17:
        return  False
    min_val,max_val = largest_and_smallest(1,17,6)
    if min_val != 1 or max_val != 17:
        return  False
    min_val,max_val = largest_and_smallest(1,1,2)
    if min_val != 1 or max_val != 2:
        return  False
    min_val,max_val = largest_and_smallest(1,1,1)
    if min_val != 1 or max_val != 1:
        return False
    min_val,max_val = largest_and_smallest(5,4,3)
    if min_val != 3 or max_val != 5:
        return False

    return True

print(check_largest_and_smallest())