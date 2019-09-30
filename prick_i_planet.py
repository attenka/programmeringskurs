import turtle

def prick_i_planet():
    sissi = turtle.Turtle()
    print("Vart på planet ritar man en prick?")
    x = int(input("Ange X"))
    y = int(input("Ange Y"))
    sissi.penup()
    sissi.setpos(x,y)
    sissi.pos()
    sissi.dot()
    sissi.write(x,y)

prick_i_planet()
    
    
