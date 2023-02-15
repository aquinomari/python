import random


numero_maximo = input("Escolha o número máximo: ")

if numero_maximo.isdigit():
    numero_maximo = int(numero_maximo) 

    if numero_maximo <= 0:
        print("Coloque um número maior que 0 na próxima vez!")
        quit()
else:
    print("Coloque um número na próxima vez!")
    quit()

random_number = random.randint(0, numero_maximo)
tentativas = 0

while True:
    tentativas += 1
    tentativa_usu = input("Faça uma tentativa: ")
    if tentativa_usu.isdigit():
        tentativa_usu = int(tentativa_usu)  
    else:
        print("Coloque um número na próxima vez!")
        continue

    if tentativa_usu == random_number:
        print("Você acertou!")
        break
    elif tentativa_usu > random_number:
            print("dica: o número é menor que esse")
    else:
            print("dica: o número é maior que esse")

print("Você acertou em", tentativas, "tentativas!")

if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
