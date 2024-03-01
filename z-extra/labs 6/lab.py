user_input = 1
with open( 'file_name.txt', 'w') as f:
    g = open('file_another.txt', 'w')
    while user_input != '7':
        user_input = input('please type a number: ')
        f.write(user_input + '\n')
        g.write(user_input + '\n')
    g.close()