from random import randint
cpu = randint(1,6)
print("Vou pensar em um número entre 1 e 6: ")
acertou = False
while not acertou:
    jogador = int(input("Qual número eu pensei ? :"))
    if jogador == cpu:
        acertou=True
        print("Acertou!!!")
    else:
        if jogador > cpu:
            print("O número é um pouco menor.")
        elif jogador < cpu:
            print("O número é um pouco maior.")
