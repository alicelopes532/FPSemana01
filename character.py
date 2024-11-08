# [['Raul', (5, 10)], ['Maria', (15, 5)], ['Carlos', (10, 10)]]

#Criou-se um array vazio para ser preenchido
jogadores = []

#Os elementos vão sendo introduzidos até ao limite de 3, o int faz com que seja valores numericos. O append cria o formato desejado e é imprimido
while len(jogadores) < 3:
    name = input("Enter name: ")
    attack = int(input("Enter value: "))
    defense = int(input("Enter value: "))

    jogadores.append([name, (attack, defense)])

print(jogadores)

#O sorted faz com que a lista seja organizada, com o lambda a expecificar o elemento que irá ser organizado pelo valor do tuplo, e o reverse para fazer uma ordem decrescente
lista_ordenada_atk = sorted(jogadores, key=lambda x: x[1][0], reverse=True)
lista_ordenada_def = sorted(jogadores, key=lambda x: x[1][1], reverse=True)

print(lista_ordenada_atk)
print(lista_ordenada_def)
