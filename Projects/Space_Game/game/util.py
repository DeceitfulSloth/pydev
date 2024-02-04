import math


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def apply_zoom(x, width, zoom):
    return ((zoom*(x-(width/2))) + (width/2))

print(apply_zoom(1440, 1920, 2))