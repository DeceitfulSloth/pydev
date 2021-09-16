import pyglet
from . import util


class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""
    

    


    def __init__(self, global_x_position, global_y_position, CAMERA_POSITION, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        self.isFocus = False

        
        self.global_x_position = global_x_position
        self.global_y_position = global_y_position

        self.x = self.global_x_position + CAMERA_POSITION[0]
        self.y = self.global_y_position + CAMERA_POSITION[1]

    def move(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.global_x_position += self.velocity_x * dt
        self.global_y_position += self.velocity_y * dt

        

        return self.global_x_position, self.global_y_position

        

    def render(self, CAMERA_POSITION, SCREEN_SIZE, ZOOM):
        
        self.scale = ZOOM
        
        un_zoomed_x = ((self.global_x_position - CAMERA_POSITION[0]) + SCREEN_SIZE[0]/2)
        un_zoomed_y = (self.global_y_position - CAMERA_POSITION[1]) + SCREEN_SIZE[1]/2

        self.x = util.apply_zoom(un_zoomed_x, SCREEN_SIZE[0], ZOOM)
        self.y = util.apply_zoom(un_zoomed_y, SCREEN_SIZE[1], ZOOM)