import turtle

ventana = turtle.Screen()
ventana.title("proyecto 1") 
ventana.bgcolor("white")  
tortuga = turtle.Turtle() 
tortuga.speed(1) 

#dibujar un triangulo

for _ in range(3):
    tortuga.forward(100) 
    tortuga.left(120) 


ventana.exitonclick()  