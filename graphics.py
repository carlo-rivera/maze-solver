from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self._root_widget = Tk()
        self._root_widget.title = "Maze Solver"
        self._canvas = Canvas(self._root_widget, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self._root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root_widget.update_idletasks()
        self._root_widget.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        
    def close(self):
        self._running = False

    def draw_line(self, line, fill_color: str="black"):
        line.draw(self._canvas, fill_color)
        
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )

