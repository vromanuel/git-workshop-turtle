from turtle import *

penup()
home()
screen = Screen()
screen.setup(1000, 600)
write("CODE NETWORK", align="center", font=("Arial", 24, "bold"))


goto (88,88)
color("green")
write("Ggoofy", align="center", font=("Times New Roman", 24, "bold"))
for num in (range(100)):
    forward(10)
    left(10)

goto(-300,0)
color("green")
write("Anthony", align = "center", font = ("Times New Roman", 16))

goto(350, -200)
color("medium purple")
write("Boop", align="center", font=("Comic Sans", 9, "italic"))

goto(123,123)
color("dodgerblue")
write("Corey McCormick", align='center', font=("Comic Sans MS", 14))

done()
