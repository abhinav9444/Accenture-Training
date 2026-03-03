import turtle
paul = turtle.Turtle()
for side in [1, 2, 3, 4]:
    paul.forward(100)
    paul.right(90)
    for side in [1, 2, 3, 4]:
        paul.forward(10)
        paul.right(90)