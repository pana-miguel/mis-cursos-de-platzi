#turtle es una libreria que nos permite dibujar en una ventana grafica con un cursor que se mueve en la pantalla 
#dependiendo de las instrucciones que le demos 
import turtle

ventana = turtle.Screen() #creamos una ventana
ventana.title("proyecto 1") #le damos un titulo a la ventana
ventana.bgcolor("white") #le damos un color d efondo a la ventana 
tortuga = turtle.Turtle() #creamos el objeto tortuga
tortuga.speed(1) #le damos una velocidad a la torutga

#dibujar un cuadrado

for _ in range(4): #un ciclo que se repite 4 veces
    tortuga.forward(100) #la tortuga avanza 100 pixeles
    tortuga.left(90) #la tortuga gira 90 grados a la izquierda


ventana.exitonclick() #esta funcion sirve para que la ventana se cierre solo cuando aga clicl en ella 