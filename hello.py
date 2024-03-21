from turtle import *
penup()
home()
screen = Screen()
screen.setup(1000, 600)
write("CODE NETWORK", align="center", font=("Arial", 24, "bold"))

goto(400, 298)
shape("turtle")
color("yellow")
write("Kim", align='center', font=("Arial", 12, "normal"))
for i in range(4):
    forward(100)
    left(90)

done()
