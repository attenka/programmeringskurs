import turtle

def fargcirklar(farger,bredd,vinkel):
    
    sissi = turtle.Turtle()

    for farg in farger:
        sissi.color(farg)
        sissi.begin_fill()
        sissi.circle(bredd)
        sissi.left(vinkel)
        sissi.forward(100)
        sissi.end_fill()


farglista = ["red","black","blue","green","yellow","pink"]
fargcirklar(farglista,40,60)

