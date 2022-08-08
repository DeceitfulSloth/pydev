import pyglet
import random
from pyglet import image
from pyglet import resource

from pyglet.graphics import Batch
from . import physicalobject, resources, util


def stars(screen_size, num, main_batch, camera_position):
    star_list = []

    for i in range(num):
        s = physicalobject.PhysicalObject(random.randint(-screen_size[0] / 2, screen_size[0] / 2),
                                          random.randint(-screen_size[1] / 2, screen_size[1] / 2),
                                          camera_position, isBackground=True, img=resources.star_image,
                                          batch=main_batch)

        star_list.append(s)

    return star_list


def other_ship(x, y, camera_position, my_batch):
    return physicalobject.PhysicalObject(x, y, camera_position, batch=my_batch, img=resources.other_ship_image)
        
        