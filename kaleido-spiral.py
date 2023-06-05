import turtle
from itortools     import cycle
colors = cycle(('red','blue', 'orange','yellow','purple','green'))


def draw_circle(size,angles,shift):
     turtle.pencolor(next(colors))
     turtle.circles(size)
     turtle.right(angles)
     turtle.forward(shift)
     draw_circle(size+5,angle+1,shift+1)

     turtle.bgcolor('black')
     turtle.speed('fast')
     turtle.pensize(4)
     draw_circle(30,0,1)
                
