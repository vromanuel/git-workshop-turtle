from turtle import *
penup()
home()
screen = Screen()
screen.setup(1000, 600)
write("CODE NETWORK", align="center", font=("Arial", 24, "bold"))

goto(200, 45)
shape("turtle")
color("red")
write("Kim", align='center', font=("Arial", 12, "normal"))
pendown()
for i in range(4):
    forward(100)
    left(90)

done()
