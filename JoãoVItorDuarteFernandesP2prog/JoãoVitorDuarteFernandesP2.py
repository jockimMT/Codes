L1 = []
L2 = []
L3 = []
OrderedL3 = []
temp = []

#Toma valores da lista 1
while True:
    n = eval(input("Digite os valores da Lista 1 (0 para finalizar a lista): "))
    L1.append(n)
    
    if n == 0:
        L1.remove(0)
        break 
#Toma valores da lista 2
while True:
    n = eval(input("Digite os valores da Lista 2 (0 para finalizar a lista): "))
    L2.append(n)
    
    if n == 0:
        L2.remove(0)
        break 

#Tamanho de cada lista
T1 = len(L1)
T2 = len(L2)

#Comparação de tamnhaos e criação da lista 3
if len(L1) >= len(L2):
    
    for i in range (len(L2)):
        L3.append(L1[i])
        L3.append(L2[i])
    for i in range(T2,T1):
        L3.append(L1[i])

if len(L2) > len(L1):
    
    for i in range (len(L1)):
        L3.append(L1[i])
        L3.append(L2[i])
    for i in range(T1,T2):
        L3.append(L2[i])

#Criação de lista temporária pra criação da lista ordenada
temp = L3.copy()

#Criação da lista ordenada
while len(temp) >= 1:
    menor = temp[0]
    for i in range(len(temp)):
        if temp[i] < menor:
            menor = temp[i]
    OrderedL3.append(menor)
    temp.remove(menor)

#Listas
print("Lista 1: \n", L1)
print("Lista 2: \n", L2)
print("Lista 3: \n", L3)
print("Lista 3 ordenada: \n", OrderedL3)
