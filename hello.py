from turtle import *

penup()
home()
screen = Screen()
screen.setup(1000, 600)
write("CODE NETWORK", align="center", font=("Arial", 24, "bold"))
goto(250,-170)
color("coral")
write("Navaneeth", align='center', font=("Helvetica", 15))

goto(300,-200)
color("pink")
write("Alex", align="center", font=("Comic Sans MS", 16))

goto (88,88)
color("green")
write("Ggoofy", align="center", font=("Times New Roman", 24, "bold"))
pendown()
for num in (range(100)):
    forward(10)
    left(10)
penup()

goto(-300,0)
color("green")
write("Anthony", align = "center", font = ("Times New Roman", 16))

goto(350, -200)
color("medium purple")
write("Boop", align="center", font=("Comic Sans", 9, "italic"))

goto(123,123)
color("dodgerblue")
write("Corey McCormick", align='center', font=("Comic Sans MS", 14))

goto(200, 45)
shape("turtle")
color("red")
write("Kim", align='center', font=("Arial", 12, "normal"))

pendown()
for i in range(4):
    forward(100)
    left(90)
penup()

goto(250, 150)
color("black")
write("Daniel Willoughby", align='center', font=("Verdana", 10))

goto(116, 116)
write("Reilly", align="center", font=("papyrus", 13, "bold"))
done()

goto(150, 150)
write("Manny", align="center", font=("comic sans", 13, "bold"))
done()