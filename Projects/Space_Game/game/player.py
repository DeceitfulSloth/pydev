import re
import pyglet, math
from pyglet import resource
from pyglet.window import key
from . import physicalobject, resources


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

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.Q]:
            print('Q')
        
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            self.image = resources.player_image_thrust
        else:
            self.image = resources.player_image

        return (x1, y1)

    


