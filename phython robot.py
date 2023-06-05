import turtle as s
def rectangle(horizontal,vertical,color):
    s.pendown()
    s.pensize(1)
    s.color(color)
    s.begin_fill
    for counter in range(1,3):
        s.forward(horizontal)
        s.right(90)
        s.forward(vertical)
        s.right(90)
        s.end_fill()
        s.penup()
        s.speed('slow')
        s.bgcolor('dodger blue')
        #feet
        s.goto(-100,-150)
        rectangle(50,20,'blue')
        s.goto(-30,-150)
        rectangle(50,20,'blue')
        #legs
        s.goto(-25,-50)
        rectangle(15,100,'grey')
        s.goto(-55,-50)
        rectangle(-15,100,'grey')
        #arms
        s.goto(-150,70)
        rectangle(60,15,'grey')
        s.goto(-150,110)
        rectangle(15,40,'grey')
        s.goto(10,70)
        rectangle(60,15,'grey')
        s.goto(55,110)
        rectangle(15,40,'grey')
        #neck
        s.goto(-50,120)
        rectangle(15,20,'grey')

        
def rectangle(horizontal,vertical,color):
    s.pendown()
    s.pensize(1)
    s.color(color)
    s.begin_fill
    for counter in range(1,3):
        s.forward(horizontal)
        s.right(90)
        s.forward(vertical)
        s.right(90)
        s.end_fill()
        s.penup()
        s.speed('slow')
        s.bgcolor('dodger blue')
        #feet
        s.goto(-100,-150)
        rectangle(50,20,'blue')
        s.goto(-30,-150)
        rectangle(50,20,'blue')
        #legs
        s.goto(-25,-50)
        rectangle(15,100,'grey')
        s.goto(-55,-50)
        rectangle(-15,100,'grey')
        #arms
        s.goto(-150,70)
        rectangle(60,15,'grey')
        s.goto(-150,110)
        rectangle(15,40,'grey')
        s.goto(10,70)
        rectangle(60,15,'grey')
        s.goto(55,110)
        rectangle(15,40,'grey')
        #neck
        s.goto(-50,120)
        rectangle(15,20,'grey')
        #head
        s.goto(-85,170)
        rectangle(80,50,'red')
        #eyes
        s.goto(-60,160)
        rectangle(30,10,'white')
        s.goto(-55,155)
        rectangle(5,5,'black')
        s.goto(-40,155)
        rectangle(5,5,'black')
        #mouth
        s.goto(-65,135)
        rectangle(40,5,'black')
        s.hideturtle()
