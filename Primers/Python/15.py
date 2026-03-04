import turtle
# howard = turtle.Turtle()
# for side in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     howard.forward(side * 10)
#     howard.right(90 - side)

import turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
for side in range(50):
    t.forward(side)
    t.right(45)
t.penup()
t.left(45)
t.forward(100)
t.pendown()
for side in range(50):
    t.forward(side)
    t.right(45)