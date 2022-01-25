import math

vetorPar = []
vetorImpar = []

i = 2

for i in range(2,21):
    if (i % 2 == 0):

        vetorPar.append(i**2)

for i in range(10, 20):
    vetorImpar.append(i)


somaVetorPar = 0
for i in vetorPar:
    somaVetorPar = i + somaVetorPar

somaVetorImpar = 0
for i in vetorImpar:
    somaVetorImpar = i + somaVetorImpar

somaTotal = somaVetorImpar + somaVetorPar

print(f'Soma do vetor par {somaVetorPar}')
print(f'soma do vetor impar: {somaVetorImpar}')
print(f"O valor da soma dos dois vetores é {somaTotal}")