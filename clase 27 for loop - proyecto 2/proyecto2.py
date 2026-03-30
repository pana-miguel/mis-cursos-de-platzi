#sabiendo el angulo interno de las puntas de las estrellas se puede calcular los nagulos para hacerla 
#solo restando ese angulo a los 180 grados para que la tortuga en este caso gire en el angulo correcto para hacer la estrella 

import turtle

ventana = turtle.Screen()
ventana.title("proyecto 2")
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(2)

for _ in range(5):
    tortuga.forward(150)
    tortuga.right(144)

ventana.exitonclick()