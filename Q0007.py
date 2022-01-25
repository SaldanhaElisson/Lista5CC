
# Online Python - IDE, Editor, Compiler, Interpreter
import random
numeroAleatorio = []
numerosPares = []
numerosImpares = []

for i in range(0, 10):
    numeroAleatorio.append(random.randint(0, 999))

for numero in numeroAleatorio:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)
print(numerosImpares)
print(numerosPares)
        
print(f'Existem {len(numerosPares)} pares e {len(numerosImpares)} impares')
        


    

    
