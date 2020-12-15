import turtle

ninja = turtle.Turtle()
screen = turtle.Screen()

bg_color = input("What color would you like the background to be?")
ninja_color = input("What color would you like ninja to be?")

screen.bgcolor(bg_color)
ninja.color(ninja_color)

ninja.forward(200)
ninja.left(90)
ninja.forward(200)
ninja.left(90)
ninja.forward(200)
ninja.left(90)
ninja.forward(200)
ninja.left(90)

kid = turtle.Turtle()
kid_color = input("What color would you like kid to be?")
kid.color(kid_color)

kid.back(200)
kid.left(90)
kid.back(200)
kid.left(90)
kid.back(200)
kid.left(90)
kid.back(200)
kid.left(90)

screen.exitonclick()
