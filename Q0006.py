
# Online Python - IDE, Editor, Compiler, Interpreter
import random
numeroAleatorio = []

for i in range(0, 10):
    numeroAleatorio.append(random.randint(0, 999))

numeroDeEntrada = int(input('Digite um numero para ser verificado: '))

if numeroDeEntrada in numeroAleatorio:
    print(f'O numero {numeroDeEntrada} existe no vetor')
else:
    print(f'O numero {numeroDeEntrada} não existe no vetor: {numeroAleatorio}')
    
