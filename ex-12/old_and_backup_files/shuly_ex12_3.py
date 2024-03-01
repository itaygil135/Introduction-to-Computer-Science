import tkinter
import random

CANVAS_SIZE = 400
CIRCLE_SIZE = 30
STEP_SIZE = 0.4
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "black", "gray"]
COLLISION_SLOWDOWN = 0.95


class MyApp:
    def __init__(self):
        self._root = tkinter.Tk()
        self._canvas = tkinter.Canvas(self._root, width=CANVAS_SIZE, height=CANVAS_SIZE, highlightbackground='black')
        self._canvas.pack()
        button = tkinter.Button(self._root, text="Add", font=("Courier", 20), command=self._add_circle)
        button.pack()

        self._circle = []

    def _add_circle(self):
        x = random.randrange(CANVAS_SIZE - CIRCLE_SIZE)
        y = random.randrange(CANVAS_SIZE - CIRCLE_SIZE)
        circ = self._canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, fill=random.choice(COLORS))
        self._circle.append([circ, 0, 0])
        if len(self._circle) == 1:
            self._move()

    def _move(self):
        for circle in self._circle:
            dx, dy = self._get_circle_move(circle)
            self._canvas.move(circle[0], dx, dy)
        self._root.after(10, self._move)  # not calling self._move()  but trigger it self._move in 10 msec

    def _get_circle_move(self, circle):
        x1, y1, x2, y2 = self._canvas.coords(circle[0])
        circle[1] += (random.randrange(1)-0.5)*STEP_SIZE
        circle[2] += (random.randrange(1)-0.5)*STEP_SIZE
        dx = circle[1]
        dy = circle[2]

        if x1+dx < 0 or x2+dx > CANVAS_SIZE:
            dx = 0
            circle[1] = -circle[1] * COLLISION_SLOWDOWN
        if y1+dy < 0 or y2+dy > CANVAS_SIZE:
            dy = 0
            circle[2] = -circle[2] * COLLISION_SLOWDOWN
        return dx, dy

    def start(self):
        self._root.mainloop()


app = MyApp()
app.start()
