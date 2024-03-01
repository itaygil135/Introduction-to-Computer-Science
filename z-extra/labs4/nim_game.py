
# ask from which row to take
From Itai Warshavsky to Me:  (Privately) 04:50 PM
"""

Create
board
with 3 rows, 5 columns
matches = [5, 5, 5]
| | | | |
| | | | |
| | | | |

for i in matches:
    print("|" * i)

"""

matches = [5,5,5]

def print_board():
    for i in matches:
        print("|"*i)

def get_input():
    row = 0
    num = 0
    while True:
        row,num = input("Please choose a row and the number of matches: ").split()
        row = int(row)
        num = int(num)

        if row > len(matches) - 1:
            print("Bad row")
            continue
        elif matches[row] == 0:
            print("Empty row.")
            continue
        elif num > matches[row]:
            num = matches[row]
        else:
            break

    matches[row] -= num

    for i in matches:
        if i > 0:
            pass












# ask from which row to take
