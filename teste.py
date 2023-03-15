import turtle

# função para desenhar um quadrado

def quadrado(tamanho):
    for i in range(4):
        turtle.forward(tamanho)
        turtle.left(90)

# função para desenhar um triângulo

def triangulo(tamanho):
    for i in range(3):
        turtle.forward(tamanho)
        turtle.left(120)

# função para desenhar um círculo

def circulo(tamanho):
    turtle.circle(tamanho)

# fazer um circulo dentro de um triângulo

def circulo_triangulo(tamanho):
    triangulo(tamanho)
    turtle.penup()
    turtle.forward(tamanho//2)
    turtle.pendown()
    circulo(tamanho//4)

circulo_triangulo(100)

# fazer uma linha no meio do triângulo

turtle.left(90)
turtle.forward(80)

# terminar

turtle.mainloop()
