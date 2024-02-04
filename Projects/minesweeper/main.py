from tkinter import *
import math
import random
from PIL import Image, ImageTk
import noise

SIZE = (2000, 1200)
CANVAS_BORDER = (30, 30)
NUM_STATIONS = 40

root = Tk()
root.title("Stations")

root2 = Tk()
root2.title("Other")

root.geometry(str(SIZE[0]+60) + "x" + str(SIZE[1]+30))
root.resizable(False, False)
c = Canvas(root, width=SIZE[0], height=SIZE[1])
c.pack()

bg = noise.stacked_perlin_3(SIZE[0], SIZE[1])

img = ImageTk.PhotoImage(image=Image.fromarray(bg))
c.create_image(0, 0, image=img, anchor="nw")


def get_station_name():
    with open('resources/space_station_names.txt') as f:
        lines = f.readlines()
    return random.choice(lines)


class Station:
    station_radius = 5

    def __init__(self, width, height):
        potential_x = random.randint(0 + CANVAS_BORDER[0], width - CANVAS_BORDER[0])
        potential_y = random.randint(0 + CANVAS_BORDER[1], height - CANVAS_BORDER[1])

        # Checking here
        self.x = potential_x
        self.y = potential_y
        self.neighbors = []
        self.name = get_station_name()
        self.station_sprite = None

    def draw(self, canvas):
        # Draw stations
        self.station_sprite = canvas.create_oval(self.x - self.station_radius, self.y - self.station_radius,
                                                 self.x + self.station_radius, self.y + self.station_radius,
                                                 fill="white",)

        # Draw connections
        for n in self.neighbors:
            canvas.create_line(self.x, self.y, n.x, n.y, fill="white", width=1)

        canvas.create_text(self.x, self.y + 25, text=self.name, fill="black", font='Consolas 14 bold')

    def add_neighbours_proximity(self, stations, max_neighbours=3):
        while len(self.neighbors) < max_neighbours:
            min_d = math.inf
            next_neighbour = None
            for a in stations:
                if a != self and a not in self.neighbors:
                    x_dif = self.x - a.x
                    y_dif = self.y - a.y
                    distance = math.sqrt(math.pow(x_dif, 2) + math.pow(y_dif, 2))
                    if distance < min_d:
                        min_d = distance
                        next_neighbour = a
            self.neighbors.append(next_neighbour)
            next_neighbour.neighbors.append(self)

    def add_neighbours_direction(self, stations):
        ne = []
        se = []
        nw = []
        sw = []

        for s in stations:
            if s.x > self.x and s.y > self.y:
                se.append(s)
            if s.x > self.x and s.y < self.y:
                ne.append(s)
            if s.x < self.x and s.y > self.y:
                sw.append(s)
            if s.x < self.x and s.y < self.y:
                nw.append(s)
            else:
                pass

        c_ne = self.closest(ne)
        c_nw = self.closest(nw)
        c_se = self.closest(se)
        c_sw = self.closest(sw)

        self.neighbors = [c_ne, c_nw, c_se, c_sw]
        self.neighbors = [r for r in self.neighbors if r]

    def closest(self, others):
        min_d = math.inf
        closest_n = None

        for a in others:
            x_dif = self.x - a.x
            y_dif = self.y - a.y
            distance = math.sqrt(math.pow(x_dif, 2) + math.pow(y_dif, 2))

            if distance < min_d:
                min_d = distance
                closest_n = a

        return closest_n

    def avoid_bumping(self, other_stations):
        for a in other_stations:
            if a != self:
                while math.sqrt(math.pow(self.x - a.x, 2) + math.pow(self.y - a.y, 2)) < 20:
                    self.x += 1
                    self.y += 1


# Create stations
my_stations = []
for i in range(40):
    my_stations.append(Station(SIZE[0], SIZE[1]))

for s in my_stations:
    s.avoid_bumping(my_stations)

# Add neighbours
for s in my_stations:
    s.add_neighbours_direction(my_stations)

for s in my_stations:
    print(s.name + ": " + str(len(s.neighbors)))

# Draw to canvas "c"
for s in my_stations:
    s.draw(c)

# Render

root.mainloop()
