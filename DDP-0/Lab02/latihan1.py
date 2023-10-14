import turtle as t
import random

RADIUS = 300
CIRCLE_ANGLE = 360

divisions = 100
layers = 100

t.setheading(90)
t.speed(0)

layer_width = RADIUS / layers

for i in range(layers):
    t.penup()
    t.setpos(t.pos() + [0, layer_width])
    t.pendown()
    for j in range(divisions):
        color = [random.choice([0, 1]) for _ in range(3)]
        t.fillcolor(color)
        t.color(color)
        t.begin_fill()
        t.forward(layer_width)
        t.left(90)
        t.circle((i + 1) * layer_width, CIRCLE_ANGLE / divisions)
        t.left(90)
        t.forward(layer_width)
        t.left(90)
        t.circle(-(i * layer_width), CIRCLE_ANGLE / divisions)
        t.end_fill()
        t.left(180)
        t.circle((i * layer_width), CIRCLE_ANGLE / divisions)
        t.right(90)
t.done()
