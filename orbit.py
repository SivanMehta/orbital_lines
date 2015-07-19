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

        self.canvas.create_rectangle(0, 0, 500, 500, fill = "#0D4566", outline = "#0D4566") # space
        self.venus = Planet(250, 150, self.canvas, "red")
        self.earth = Planet(250, 100, self.canvas, "green")
        self.sun = Planet(250, 250, self.canvas, "yellow")

        self.ticks = 0
        self.done = False
        self.timer()
        root.mainloop()

    def rotate_earth(self):
        theta = math.degrees(math.pi/36000*13.0)

        x = self.earth.x - 250
        y = self.earth.y - 250

        x, y = x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

        x += 250
        y += 250

        self.earth.move_to(x, y)

        self.canvas.update()

    def rotate_venus(self):
        theta = math.degrees(math.pi/36000*8.0)

        x = self.venus.x - 250
        y = self.venus.y - 250

        x, y = x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

        x += 250
        y += 250

        self.venus.move_to(x, y)

        self.canvas.update()

    def timer(self):
        if self.done:
            print "Done!"
            return
        self.rotate_earth()
        self.rotate_venus()

        self.ticks += 1
        if self.ticks % 2 == 0:
            self.canvas.create_line(self.earth.x, self.earth.y, self.venus.x, self.venus.y, fill = "white")
        if self.ticks > 1250:
            self.done = True

        self.canvas.after(5, self.timer)


Animation()