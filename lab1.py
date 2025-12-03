#variable exercise: red circle that changes size dynamically
import py5

# starting size and direction
size = 50
grow = True

def setup():
    py5.size(400, 400)

def draw():
    global size, grow
    
    py5.background(0)
    py5.fill(0, 255, 0)
    py5.circle(200, 200, size)  # circle in the middle with changing size
    
    # make it grow or shrink
    if grow:
        size += 2   # grow
        if size >= 150:   # max size
            grow = False
    else:
        size -= 2   # shrink
        if size <= 30:    # min size
            grow = True


# variable exercise: green circle
import py5

def setup():
    py5.size(500, 500)
    py5.background(0)  # black background

def draw():
    py5.background(0)        # keep background black each frame
    py5.fill(57, 255, 20)    # neon green color
    py5.no_stroke()          # remove outline
    py5.circle(py5.mouse_x, py5.mouse_y, 40)  # circle follows the mouse
