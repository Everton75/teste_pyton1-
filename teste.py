# Importar biblioteca
import random
import os # para limpar a tela

os.system('clear') or None #limpa a tela

#Iniciando lista onde iremos guardar os números gerados 
lista = []

#Tamanho limite que queremos gerar
#tamanho_lista = 10

# Iniciando contador para controle
i = 0

#Loop para gerar 10 números
while i < 6:
    lista.append(random.randint(1,60))
    i = i + 1

# Printando lista
print(sorted(lista))
#print(len(lista))#conta itens na lista

for listas in lista:
    numero=listas
    print(numero in lista)

    