

def is_it_summer_yet(temperatur,temperature_d1,temperature_d2,temperature_d3):
    if (temperatur < temperature_d1 and temperatur < temperature_d2) \
        or (temperatur < temperature_d1 and temperatur < temperature_d3)\
        or (temperatur < temperature_d2 and temperatur < temperature_d3):
        return True
    return  False






print(is_it_summer_yet(19, 22, 21, 20))
print(is_it_summer_yet(20, 22, 21, 20))
print(is_it_summer_yet(7, 5, -2, 11))



