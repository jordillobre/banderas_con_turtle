import turtle as Turtle
import time

def draw_japan():

    Turtle.setup(700, 700)
    Turtle.bgcolor("Black")

    ancho_banda = 300
    alto_banda = 200
    color_rojo = "#FF0000"
    color_blanco = "#FFFFFF"

    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda / 2, -alto_banda/3)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    Turtle.color(color_blanco)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.goto(0, -alto_banda/6)
    Turtle.pendown()

    Turtle.begin_fill()
    Turtle.color(color_rojo)
    Turtle.circle(alto_banda/3)
    Turtle.end_fill()

   
    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()