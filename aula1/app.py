

# escola

# cadastro
import tkinter as tkinter




acesso = input('Deseja acessar o sistema? s/n >> ')

while acesso == 's':
    print("SISTEMA ESCOLA CAVALCANTI")

    nome = input("Nome Aluno 😎 >> ") # variável
    # snake_case
    nota_1 = float(input("Nota 1>>  "))
    nota_2 = float(input("Nota 2>>  "))
    nota_3 = float(input("Nota 3>>  "))
 
    # media
    lista = []
    lista.append(nota_1)
    lista.append(nota_2)
    lista.append(nota_3)

    media = sum(lista)/len(lista)

    print("O aluno(a)", nome, "possui a média" , media)

    if media >= 7:
        print(f'O {nome} Passou de ano')
    elif media >=5 and media <7:
        print(f'o {nome} está de recuperação 😢')
    else:
        print(f'o {nome} não passou de ano 🤦‍♂️...')
    acesso = input('Deseja acessar continuar? s/n >>')    

print('Até logo...')
input('clique enter para sair...')



