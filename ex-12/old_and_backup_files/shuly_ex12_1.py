import tkinter

STYLE = {"font": ("Courier", 30), "bg":"lightgray"}
class MyApp:
    def __init__(self):
        self._root = tkinter.Tk()
        self._label = tkinter.Label(self._root, **STYLE)
        self._label.pack(fill = tkinter.BOTH)
        button = tkinter.Button(self._root, text = "click me", **STYLE)
        button.pack()
        self._canvas = tkinter.Canvas(self._root, width= 250, height = 250, bg = 'blue')
        self._canvas.pack()
        self._canvas.bind("<Enter>",self._enter_event_handler)
        self._canvas.bind("<Leave>", lambda event: self._canvas.config(bg="white"))
        self._canvas.bind("<Button-1>", lambda event: self._label.configure(text = str((event.x, event.y))))

        self._label.bind("<Button-1>", lambda  event: self._label.configure(text="press"))
        self._label.bind("<ButtonRelease-1>", lambda event: self._label.configure(text="release"))
        self._label.bind("<Double-Button-1>", lambda event: self._label.configure(text="double"))
        self._label.bind("<Triple-Button-1>", lambda event: self._label.configure(text="triple"))



    def _enter_event_handler(self,event):
        self._canvas["bg"]="red"

    def start(self):
        self._root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = MyApp()
    app.start()