import pyglet
import random
from pyglet import image
from pyglet import resource

from pyglet.graphics import Batch
from . import physicalobject, resources, util


def stars(SCREEN_SIZE, num, main_batch, CAMERA_POSITION):
    star_list = []
    

    for i in range(num):
        s = physicalobject.PhysicalObject(random.randint(-SCREEN_SIZE[0]/2,SCREEN_SIZE[0]/2), random.randint(-SCREEN_SIZE[1]/2,SCREEN_SIZE[1]/2), CAMERA_POSITION, isBackground=True, img=resources.star_image, batch=main_batch)

        star_list.append(s)

    return star_list



def other_ship(x, y, CAMERA_POSITION, my_batch):
    return physicalobject.PhysicalObject(x,y,CAMERA_POSITION, batch=my_batch, img=resources.other_ship_image)
        
        