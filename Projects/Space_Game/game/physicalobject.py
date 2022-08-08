from game import resources
import pyglet
from . import util


class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, global_x_position, global_y_position, camera_position, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        self.isFocus = False
        self.base_image = self.image
        
        self.global_x_position = global_x_position
        self.global_y_position = global_y_position

        self.x = self.global_x_position + camera_position[0] + 200
        self.y = self.global_y_position + camera_position[1] + 200

    def move(self, dt):
        """This method should be called every frame."""

        self.global_x_position += self.velocity_x * dt
        self.global_y_position += self.velocity_y * dt

        return self.global_x_position, self.global_y_position

    def render(self, camera_position, screen_size, zoom):
        if zoom < 0.1:
            self.image = resources.white_circle
            self.scale = 1
        else:
            self.image = self.base_image
            self.scale = zoom
        
        un_zoomed_x = ((self.global_x_position - camera_position[0]) + screen_size[0] / 2)
        un_zoomed_y = (self.global_y_position - camera_position[1]) + screen_size[1] / 2

        self.x = util.apply_zoom(un_zoomed_x, screen_size[0], zoom)
        self.y = util.apply_zoom(un_zoomed_y, screen_size[1], zoom)