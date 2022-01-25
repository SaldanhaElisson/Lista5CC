import random
vetor10Elementos = []

for index in range(0, 10):
    vetor10Elementos.append(random.randint(0, 999))
    for i in range(0, vetor10Elementos[index]):
        if(i == vetor10Elementos[index]):
            continue
        elif(i == 1):
            continue
        elif(i == 0):
            continue
        dividindoElement = vetor10Elementos[index] % i
        quociente = vetor10Elementos[index] / i

        if(dividindoElement == 0):
            print(f'{vetor10Elementos[index]} dividido por {i} é igual a {dividindoElement}: não é primo {quociente}' )
            break
  
