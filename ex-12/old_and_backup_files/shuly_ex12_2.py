import tkinter

class MyApp:
    def __init__(self):
        self._root = tkinter.Tk()
        self._var = tkinter.StringVar()
        self._var.trace("w", lambda  *args: print("changed to:", self._var.get()))

        self._slider = tkinter.Scale(self._root, variable = self._var)
        self._slider.pack()

        self._lable = tkinter.Label(self._root, textvariable = self._var)
        self._lable.pack()

        self._entry = tkinter.Entry(self._root, width = 5, textvariable = self._var)
        self._entry.pack()

    def start(self):
        self._root.mainloop()


app =MyApp()
app.start()