import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple","blue" , "grey", "pink", "maroon", "yellow", "cyan"]

# Write whatever code you want here!
pen = turtle.Turtle()
pen.width(2)
pen.speed(0)
pen.hideturtle()
for objs in rainbow:
    pen.color(objs)
    for vertices in [1,2,3,4,5]:
        pen.forward(15)
        pen.left(72)
    pen.penup()
    pen.left(30)
    pen.forward(25)
    pen.pendown()
