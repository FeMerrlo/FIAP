matriz=[]
 
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))

for i in range(0, linhas, 1):
    matriz.append([])
 

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)
N = int(input("Digite um número para multiplicar a matriz: "))
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        r = matriz[l] [c] = matriz[l] [c] * N
        matriz[l].append(r)
print(matriz)
 

for i in range(0, linhas, 1):
    print(matriz[i])


for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        print(matriz[l][c])
