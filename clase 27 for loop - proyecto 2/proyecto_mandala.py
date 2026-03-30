#esta es una estrella con 15 puntas

import turtle

ventana = turtle.Screen()
ventana.title("proyecto 2")
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(3)

for _ in range(15):
    tortuga.forward(250)
    tortuga.right(168)

ventana.exitonclick()