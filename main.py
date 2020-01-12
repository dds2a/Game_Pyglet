import pyglet
from pyglet import gl
from pyglet.window import key
from pyglet.gl import *
import math

level = [
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--------------------------',
    '--- -  ------------  - ---',
    '--- -  ------------  - ---',
    '--- ------------------ ---',
    '---- ---------------- ----',
    '-----                -----',
    '--------------------------'
]
level.reverse()

W, H = 780, 630
BG_COLOR = (0.75, 0.75, 0.75, 1.)

RADIUS = 30
SIZE = 30
COLOR = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1)
x = W // 2
y = H // 2

window = pyglet.window.Window(width=W, height=H, caption='Game')
window.set_location(5, 30)
window.set_mouse_visible(visible=False)
counter = pyglet.window.FPSDisplay(window=window)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

# start QUADS
x = y = 0
for raw  in level:
    for col in raw: 
        if col == '-':
            polygon = batch.add(
                4, pyglet.gl.GL_QUADS,  background,
                ('v2f', [x, y, x, y + SIZE, x + SIZE, y + SIZE, x + SIZE, y]),
                ('c3f', COLOR)
            )
        x += SIZE
    y += SIZE
    x = 0    
# stop QUAdsAsAAT
# start smailik
x1, y1 = W // 2, H // 2
point_list = []
for angle in (0, 360, 10):
    rads = math.radians(angle)
    s = RADIUS * math.sin(rads)
    c = RADIUS * math.cos(rads)
    point_list.append(x1 + c)
    point_list.append(y1 + s)
NP = len(point_list) // 2
circle_list = batch.add(
    NP, pyglet.gl.GL_TRIANGLE_FAN, foreground,
    ('v2f', point_list),
    ('c4f', (0, 1, 0, .5) * NP)
)
# stop SMAiLIkKK

def update(dt):
    pass


@window.event
def on_draw():
    window.clear()
    batch.draw()
    counter.draw()

gl.glClearColor(*BG_COLOR)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
