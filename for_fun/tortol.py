import turtle as t

for i in range(10):
    t.circle(100)
    t.left(90)
    t.penup()
    t.forward(100 / 10)
    t.pendown()
    t.right(90)

t.done()
