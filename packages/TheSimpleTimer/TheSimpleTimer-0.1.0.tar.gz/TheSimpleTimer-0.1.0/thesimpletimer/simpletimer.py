import tkinter as tk
import time


class Point:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x + other.x), int(self.y + other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x + other), int(self.y + other))

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x - other.x), int(self.y - other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x - other), int(self.y - other))

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x / other.x), int(self.y / other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x / other), int(self.y / other))

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x * other.x), int(self.y * other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x * other), int(self.y * other))

    def __eq__(self, other):
        if isinstance(other, Point):
            return True if self.x == other.x and self.y == other.y else False

    def __hash__(self):
        return hash((self.x, self.y))


WIN = Point(600, 600)
SPN = Point(0, 0)


class App(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initUI()
        self.timer_update()

    def initUI(self):
        self.root.geometry(f"{WIN.x}x{WIN.y}+{SPN.x}+{SPN.y}")
        self.root.title("Stop Watch")

        self.timer = 0
        self.start = None
        self.end = None
        self.run = False

        self.time_display = tk.Label(self.root, text="Unkown Time")
        self.time_display.pack()

        self.but = tk.Button(
            self.root, text="Start", command=self.switch, width=50, height=25
        )
        self.but.pack()

    def timer_update(self):
        if self.run:
            self.timer = round(time.time() - self.start, 2)
            self.time_display.config(text=str(self.timer))
            but_text = "Stop"
        else:
            but_text = "Start"

        self.but.config(text=but_text)
        self.root.after(100, self.timer_update)

    def switch(self):
        self.start = time.time()
        self.run = False if self.run else True
