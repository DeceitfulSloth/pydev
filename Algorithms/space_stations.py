#Import the library
from tkinter import *
import random
import math

#Create an instance of tkinter frame
win= Tk()

# Define constants
WIDTH = 1200
HEIGHT = 800
TOP_MARGIN = 10
BOTTOM_MARGIN = 10
LEFT_MARGIN = 10
RIGHT_MARGIN = 10

#Define the geometry of window
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Fix random state
random.seed(42)

#Create a canvas object
c= Canvas(win,width=WIDTH, height=HEIGHT, bg="black")
c.pack()

# Defines a station (currently just a circle)
class Station:
    x = 0
    y = 0
    color = ""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "white"
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, station):
        return int(math.sqrt(pow(self.get_x() - station.get_x(), 2) + pow(self.get_y() - station.get_y(),2)))

    def set_color(self, c):
        self.color = c
    
    def get_color(self):
        return self.color


#Draw an Oval in the canvas
def draw_circle(canvas, x, y, radius, color):
    c.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

def draw_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, dash=(4, 2), fill="cyan")


def is_within(a, b, r):
    if (a + r) > b and (a - r) < b:
        return True
    else:
        return False


# Generate a list of 50 stations
stations = []
for i in range(100):
    stations.append(Station(random.randint(LEFT_MARGIN, WIDTH - RIGHT_MARGIN), random.randint(TOP_MARGIN, HEIGHT - BOTTOM_MARGIN)))

print(f'There are {len(stations)} stations.')

# Mark overlapping stations
for i in stations:
    for j in stations:
        if i != j and i.distance(j) < 50:
            stations.remove(j)
            

            
print(f'There are {len(stations)} stations.')

# Generate station connections
connections = []
for i in range(len(stations)):
    for j in range(i, len(stations)):
        if stations[i].distance(stations[j]) < 200:
            connections.append((stations[i],stations[j]))

print(f'There are {len(connections)} connections.')

# Display stations
for i in stations:
    draw_circle(c,i.get_x(), i.get_y(), 5, i.get_color())

for i in connections:
    draw_line(c, i[0].get_x(), i[0].get_y(), i[1].get_x(), i[1].get_y())

win.mainloop()

