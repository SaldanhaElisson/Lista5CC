from collections import Counter
import random

numerosRepetido = []


for i in range(0,10):
    numerosRepetido.append(random.randint(1,10))

c = Counter(numerosRepetido)

for numero, repetição in c.items():
    if repetição > 1:
        print(f'O {numero} repete {repetição} vezes na lista')
