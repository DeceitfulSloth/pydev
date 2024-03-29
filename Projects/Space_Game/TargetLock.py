import pyglet
from game import load, player

# Set up a window
game_window = pyglet.window.Window()
game_window.set_fullscreen(True)


SCREEN_SIZE = game_window.get_size()
CAMERA_POSITION = SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2
ZOOM = 1
PAUSED = False

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite and other ship
player_ship = player.Player(0, 0, CAMERA_POSITION, batch=main_batch)
other_ship = load.other_ship(500, 0, CAMERA_POSITION, main_batch)

# Store all objects that update each frame in a list
game_objects = [player_ship] + [other_ship]

# Tell the main window that the player object responds to events
game_window.push_handlers(player_ship.key_handler)


@game_window.event       
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global ZOOM
    if scroll_y == 1.0 and ZOOM < 1.5:
        ZOOM = ZOOM * 1.1
    elif scroll_y == -1.0:
        ZOOM = ZOOM * 0.9


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    global CAMERA_POSITION
    global SCREEN_SIZE
    global ZOOM
    global PAUSED
    
    # Allow dynamic camera change.
    if PAUSED is False:
        for obj in game_objects:
            # Move camera to player ship
            # obj.update(dt, SCREEN_SIZE, CAMERA_POSITION)
            pos = obj.move(dt)
            if obj.isFocus:
                CAMERA_POSITION = pos
            
    # Render all objects    
    for obj in game_objects:
        obj.render(CAMERA_POSITION, SCREEN_SIZE, ZOOM)

    
if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
