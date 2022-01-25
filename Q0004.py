
# Online Python - IDE, Editor, Compiler, Interpreter

fibonacci = []

valorAnterior = 0 
valorAntesDoAnterior = 1

for i in range(0, 20):
    valorAtual = valorAnterior + valorAntesDoAnterior
    valorAntesDoAnterior = valorAnterior
    valorAnterior = valorAtual
    
    fibonacci.append(valorAtual)
    
print(fibonacci)
    
