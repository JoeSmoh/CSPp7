import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

painter.penup()
painter.goto(50,-10)
painter.pendown()

circlesz=int(input("what size do you want the circles?"))

painter.circle(circlesz)

painter.penup()
painter.goto(-20,10)
painter.pendown()

painter.circle(circlesz)

wn = trtl.Screen()
wn.mainloop()