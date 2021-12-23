import re
import pyglet, math
from pyglet import resource
from pyglet.window import key
from . import physicalobject, resources, util


class Player(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        # Set some easy-to-tweak constants
        self.thrust = 300.0
        self.rotate_speed = 200.0

        self.isFocus = True

        # Let pyglet handle keyboard events for us
        self.key_handler = key.KeyStateHandler()

    def move(self, dt):
        # Do all the normal physics stuff
        x1, y1 = super(Player, self).move(dt)

        
        if self.key_handler[key.A]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.D]:
            self.rotation += self.rotate_speed * dt
        
        if self.key_handler[key.W]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            self.image = resources.player_image_thrust
        else:
            self.image = resources.player_image

        return x1, y1


    def render(self, CAMERA_POSITION, SCREEN_SIZE, ZOOM):
        if ZOOM < 0.1:
            self.image = resources.white_circle
            self.scale = 1
        else:
            #self.image = resources.player_image
            self.scale = ZOOM
        
        un_zoomed_x = ((self.global_x_position - CAMERA_POSITION[0]) + SCREEN_SIZE[0]/2)
        un_zoomed_y = (self.global_y_position - CAMERA_POSITION[1]) + SCREEN_SIZE[1]/2

        self.x = util.apply_zoom(un_zoomed_x, SCREEN_SIZE[0], ZOOM)
        self.y = util.apply_zoom(un_zoomed_y, SCREEN_SIZE[1], ZOOM)
    


