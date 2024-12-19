
snake = [
    [5,10],
    [6,10],
    [7,10],
        ]

print(snake)
print('\n\n')

head = snake[0].copy() # recebe a copia da cabeça da cobrinha
head [0] -= 1 # faz a cabeça da cobrinha -1 

print(snake)
print(head)
print('\n\n')

snake.insert(0,head)

print(snake)

snake.pop()
print(snake)
