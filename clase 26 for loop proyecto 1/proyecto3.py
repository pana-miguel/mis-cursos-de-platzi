import turtle

ventana = turtle.Screen()
ventana.title("proyecto 1") 
ventana.bgcolor("orange")  
tortuga = turtle.Turtle() 
tortuga.speed(3) 

#dibujar un circulo 

for _ in range(36):
    tortuga.forward(10) 
    tortuga.left(10) 


ventana.exitonclick()  