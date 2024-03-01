
def knapsack_helper(items, i , max_weight, weight, value):
    #if we have exceeded out weight, this is not a valid solution
    if weight > max_weight:
        return 0
    #if we have reached the end of the list, return the current value
    if i == len(items):
        return value

    #first try adding the i'th element, update weight and value and continue
    value_with_index = knapsack_helper(items,
                                        i+1,
                                        max_weight,
                                        weight + items[i][0],
                                        value + items[i][1])

    #skip over the ith element and continue trying with the rest
    value_without_index = knapsack_helper(items,
                                          i+1,
                                          max_weight,
                                          weight,
                                          value)

    #pick the better value of the two and return it
    return max(value_with_index, value_without_index)

def knapsack(items, max_weight):
    return knapsack_helper(items, 0, max_weight, 0 ,0)



if __name__ == '__main__':
    items = [(2,4),(5,10),(3,7)]
    print(knapsack(items, 6))