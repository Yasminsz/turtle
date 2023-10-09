"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle

turtle = turtle.Turtle()
turtle.color('red')

for _ in [1, 2, 3]:
    turtle.shape('triangle')
    turtle.forward(120)
    turtle.right(120)
    
turtle.color('blue')
for _ in [1, 2, 3, 4]:
    turtle.shape('turtle')
    turtle.forward(120)
    turtle.right(90)