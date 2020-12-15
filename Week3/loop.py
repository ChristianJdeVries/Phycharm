import turtle

for friend in ("Thomas", "Wouter", "Jasper", "Pim"):
    invite = "Hi " + friend + ". Come to my party!"
    print(invite)

ninja = turtle.Turtle()
screen = turtle.Screen()

for _ in (0, 1, 2, 3):
    ninja.forward(50)
    ninja.left(90)

ninja.penup()
ninja.forward(100)
ninja.pendown()

for _ in range(4):
    ninja.forward(50)
    ninja.right(90)

ninja.penup()
ninja.backward(200)
ninja.pendown()

for color in ["yellow", "red", "purple", "blue"]:
    ninja.color(color)
    ninja.forward(50)
    ninja.left(90)

screen.exitonclick()
