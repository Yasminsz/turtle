"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

def desenhar_forma(turtle, forma, cor):
    turtle.shape(forma)
    turtle.color(cor)
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.backward(150)
    turtle.right(90)

turtle = turtle.Turtle()

desenhar_forma(turtle, 'turtle', 'blue')
desenhar_forma(turtle, 'triangle', 'red')
desenhar_forma(turtle, 'circle', 'green')
desenhar_forma(turtle, 'square', 'yellow')
