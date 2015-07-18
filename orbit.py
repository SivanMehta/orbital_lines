from Tkinter import Tk, Canvas
import math

class Planet():
    def __init__(self, x, y, space, color):
        self.x = x
        self.y = y
        self.space = space
        self.color = color
        self.radius = 5

        self.draw()

    def draw(self):
        self.id = self.space.create_oval(self.x - self.radius,
                                         self.y - self.radius,
                                         self.x + self.radius,
                                         self.y + self.radius,
                                         fill = self.color,
                                         outline = self.color)

    def move_to(self, x, y):
        self.space.move(self.id, x - self.x, y - self.y)
        self.x = x
        self.y = y

class Animation():
    def __init__(self):
        root = Tk()
        self.canvas = Canvas(root, height = 500, width = 500)
        self.canvas.pack()

        self.canvas.create_oval(150, 150, 350, 350)
        self.venus = Planet(250, 350, self.canvas, "red")
        
        self.canvas.create_oval(100, 100, 400, 400)
        self.earth = Planet(250, 100, self.canvas, "green")

        self.sun = Planet(250, 250, self.canvas, "yellow")

        # self.canvas.create_oval()

        self.timer()
        root.mainloop()

    def rotate_earth(self):
        theta = math.degrees(math.pi/3600*1.0)

        x = self.earth.x - 250
        y = self.earth.y - 250

        x, y = x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

        x += 250
        y += 250

        self.earth.move_to(x, y)

        self.canvas.update()

    def rotate_venus(self):
        theta = math.degrees(math.pi/3600*1.0)

        x = self.venus.x - 250
        y = self.venus.y - 250

        x, y = x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

        x += 250
        y += 250

        self.venus.move_to(x, y)

        self.canvas.update()

    def timer(self):
        self.rotate_earth()
        self.rotate_venus()
        self.canvas.after(10, self.timer)


Animation()