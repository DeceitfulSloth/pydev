#Import the library
from tkinter import *
import random
import math
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win= Tk()
win.resizable(width=False, height=False)

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
#random.seed(42)

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

def draw_line(canvas, x1, y1, x2, y2, color):
    canvas.create_line(x1, y1, x2, y2, dash=(4, 2), fill=color, width=1)


def is_within(a, b, r):
    if (a + r) > b and (a - r) < b:
        return True
    else:
        return False


# Generate a list of 50 stations
stations = []
for i in range(75):
    stations.append(Station(random.randint(LEFT_MARGIN, WIDTH - RIGHT_MARGIN), random.randint(TOP_MARGIN, HEIGHT - BOTTOM_MARGIN)))

print(f'There are {len(stations)} stations.')

# Mark overlapping stations
for i in stations:
    for j in stations:
        if i != j and i.distance(j) < 75:
            stations.remove(j)
            

            
print(f'There are {len(stations)} stations.')

# Generate simple station connections
connections = []
for i in range(len(stations)):
    for j in range(i, len(stations)):
        if stations[i].distance(stations[j]) < 200:
            connections.append((stations[i],stations[j]))


def generate_connections():
    newConnections = []
    # Generate new station connections
    for i in range(len(stations)):
        for j in range(i + 1, len(stations)):
            if stations[i].distance(stations[j]) < 200:
                newConnections.append((stations[i], stations[j], stations[i].distance(stations[j]), True))

    # Crop too long connections
    croppedConnections = []

    for i in stations:
        # Smallest connections in 4 directions
        LD_Min = float('inf')
        LU_Min = float('inf')
        RD_Min = float('inf')
        RU_Min = float('inf')
        LD_Con = None
        LU_Con = None
        RD_Con = None
        RU_Con = None


        for j in newConnections:
            if i == j[0]: # If the station under consideration is the start of the connection


                if j[0].get_x() < j[1].get_x() and j[0].get_y() < j[1].get_y():
                    if j[2] < RD_Min:
                        RD_Con = j


                elif j[0].get_x() >= j[1].get_x() and j[0].get_y() < j[1].get_y():                
                    if j[2] < LD_Min:
                        LD_Con = j

                if j[0].get_x() < j[1].get_x() and j[0].get_y() >= j[1].get_y():                
                    if j[2] < RU_Min:
                        RU_Con = j

                else:
                    if j[2] < LU_Min:
                        LU_Con = j

        croppedConnections.extend([LD_Con, LU_Con, RD_Con, RU_Con])        
    return croppedConnections

croppedConnections = generate_connections()



def render(con, stat):
    # Clear screen
    c.delete("all")

    for i in con:
        if i != None:
            draw_line(c, i[0].get_x(), i[0].get_y(), i[1].get_x(), i[1].get_y(), "cyan")

    # Display stations
    for i in stat:
        draw_circle(c,i.get_x(), i.get_y(), 8, i.get_color())

    # Draw ship
    ship= ImageTk.PhotoImage(Image.open("resources/ships/Ship_01.png"))
    c.create_image(10,10,anchor=NW, image = ship)

render(croppedConnections, stations)


def click_handler(event):
    # event also has x & y attributes
    # Add a station
    if event.num == 1:
        stations.append(Station(event.x, event.y))
        croppedConnections = generate_connections()
        render(croppedConnections, stations)

    # Delete a station
    elif event.num == 3:
        #print("x,y", event.x, event.y)
        closestStation = None
        minDistance = float("inf")
        for i in stations:
            #print("station x,y", i.get_x(), i.get_y(), math.sqrt(pow(i.get_x() - event.x, 2) + pow(i.get_y() - event.y, 2)))
            if math.sqrt(pow(i.get_x() - event.x, 2) + pow(i.get_y() - event.y, 2)) < minDistance:
                closestStation = i
                minDistance = math.sqrt(pow(i.get_x() - event.x, 2) + pow(i.get_y() - event.y, 2))
        
        stations.remove(closestStation)
        #print("closest station x,y", closestStation.get_x(), closestStation.get_y())
        croppedConnections = generate_connections()
        render(croppedConnections, stations)


def on_mousewheel(event):
    
    print(event)


c.bind_all("<MouseWheel>", on_mousewheel)




win.bind("<Button>", click_handler)
win.mainloop()
