



def make_pretty(func):
    def wrapper(line):
        print("fasdfsdfsdfsdfsdfsdfsdfsdfsdf")
        return func("***"+ line)
    return wrapper

my_print = make_pretty(print)

my_print("fsdfadsfas")
