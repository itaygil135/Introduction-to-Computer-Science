
MOVES =  {"up":   (-1,0),
          "down": (1,0),
          "left": (0,-1),
          "right":(0,1)}


def print_maze_and_path(maze, path):
    print("\n\n" + str(path) + "\n")
    for line in maze:
        for cell in line:
            print (str(cell).center(3), end = " ")
        print()

def do_move(place, change):
    return(place[0] + change[0] , place[1] + change[1])

def can_travel (point, maze):
    return     point[0] >= 0 and point[0] < len(maze)                    \
           and point[1] >= 0 and point[1] < len(maze[point[0]])          \
           and not maze[point[0]][point[1]]


def _print_all_paths_helper (start, goal, maze, path):
    if not can_travel(start, maze):
        return

    maze[start[0]][start[1]] = len(path) + 1

    if start == goal:
        print_maze_and_path(maze, path)
    else:
        for direction in MOVES:
            path.append(direction)
            new_start = do_move(start, MOVES[direction])
            _print_all_paths_helper(new_start,goal,maze,path)
            path.pop()
    maze[start[0]][start[1]] = ""

def print_all_paths(start, goal, maze):
    _print_all_paths_helper(start, goal, maze, [])


if __name__ == '__main__':

    maze = [["", "W", "", "",  ""],
            ["", "W", "", "W", ""],
            ["", "W", "", "W", ""],
            ["", "",  "", "",  ""],
            ["", "W", "", "W", ""]]

    print_all_paths((0,0),(0,2), maze)