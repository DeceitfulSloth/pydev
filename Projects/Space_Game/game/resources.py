import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Load the two ship types main resources and get them to draw centered
player_image = pyglet.resource.image("ship_01.png",rotate=90)
center_image(player_image)

# Load the two ship types main resources and get them to draw centered
player_image_thrust = pyglet.resource.image("ship_01_2.png",rotate=90)
center_image(player_image_thrust)

# Load other ship
other_ship_image = pyglet.resource.image("ship_05.png",rotate=90)
center_image(other_ship_image)


# Load background stars
#star_image = pyglet.resource.image("star.png")
#center_image(star_image)