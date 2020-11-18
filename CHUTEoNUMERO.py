from random import randint
cpu = randint(1,6)
print("vou pensar em um numero entre 1 e 6: ")
acertou = False
while not acertou:
    jogador = int(input("qual numero eu pensei ? :"))
    if jogador == cpu:
        acertou=True
        print("acertou!!!")
    else:
        if jogador > cpu:
            print("O número é um pouco menor.")
        elif jogador < cpu:
            print("O número é um pouco maior.")