import turtle
import random

def random_stjarnor(antal):
    sissi = turtle.Turtle()
    
    for a in range(antal):
        x = random.randint(0,200)
        y = random.randint(0,200)
        sissi.penup()
        sissi.setpos(x,y)

        for b in range(5):
            
            sissi.pendown()
            sissi.left(145)
            sissi.forward(20)
        sissi.penup()

random_stjarnor(20)
