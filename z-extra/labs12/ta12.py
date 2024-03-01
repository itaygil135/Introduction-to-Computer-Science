import tkinter as tk


class Counter:
    def __init__(self, display):
        self._counter = 0
        self._label = tk.Label(display, text=str(self._counter),font=("Courier", 30))
        self._button = tk.Button(display, text="+1", font=("Courier", 30), command=self.increase)

        self.pack()

    def increase(self):
        self._counter += 1
        self._label.config(text=str(self._counter))

    def pack(self):
        self._label.pack()
        self._button.pack()


class Counter2:
    def __init__(self, display):
        self._counter = 0
        self._label = tk.Label(display, text=str(self._counter), font=("Courier", 30))
        display.bind("<Key>", self.key_pressed)
        self.pack()

    def pack(self):
        self._label.pack()
        self._button.pack()

    def key_pressed(self, event):
        if event.keysym == "Up":
            self._counter += 1
        elif event.keysym == "Down":
            self._counter -= 1
        self._label.config(text=str(self._counter))

    def pack(self):
        self._label.pack()


class PalindromeChecker:
    def __init__(self, parent):
        self._word = tk.StringVar()
        self._entry = tk.Entry(parent, textvariable=self._word)
        self._button = tk.Button(parent, text="check word", command=self.check_if_palindrome)
        self._label = tk.Label(parent)
        self.pack()

    def check_if_palindrome(self):
        word = self._word.get()
        if word == word[::-1]:
            self._label.config(text=word + " is a palindrome!")
        else:
            self._label.config(text=word + " is a not palindrome :(")

    def pack(self):
        self._entry.pack()
        self._button.pack()
        self._label.pack()

def draw_circle(parent, color):
    pass


class Circle:
    CANVAS_SIZE = 200
    COLORS = ["red", "green", "blue", "yellow"]

    pass


if __name__ == "__main__":
    # ONLY UNCOMMENT ONE QUESTION AT A TIME!
    root = tk.Tk()
    # Q1
    # Counter(root)
    # # Q2
    # Counter2(root)
    # # Q3
    PalindromeChecker(root)
    # # Q4
    # draw_circle(root, 'red')
    # # Q5
    # Circle(root)
    root.mainloop()
