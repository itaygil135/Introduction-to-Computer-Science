
def get_discount_by_age(age):
    if age <= 18:
        return  0.2
    elif age >=100:
        return 1
    elif age >= 65:
        return (age/100)
    else:
        return 0


def buy_ticket(age):

    return (40 - 40*get_discount_by_age(age))


if __name__ == '__main__':
    # TODO test your code by running different use cases
    print("Basic Check")   # Delete this line

    # Part 1:
    # print(buy_ticket(25) == 40)
    # print(buy_ticket(5) == 32)
    # print(buy_ticket(101) == 0)
    # print(buy_ticket(70) == 12)
    # buy_ticket(-1)

    # Part 2:
    # print(buy_ticket(5, True) == 25)
    # print(buy_ticket(25) == 40)
    # print(buy_ticket(5) == 32)
    # print(buy_ticket(101) == 0)
    # print(buy_ticket(70) == 12)
    print(buy_ticket(100))
