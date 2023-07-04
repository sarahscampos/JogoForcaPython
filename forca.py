def jogar():
    print('-' * 30)
    print("Bem vindo ao jogo da forca")
    print('-' * 30)

jogar()

palavra_secreta = "python"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]

enforcou = False
acertou = False

print(letras_acertadas)

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip() # essas funções de string não alteram a string original/ STRINGS SÃO IMUTÁVEIS
    
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1
       


    print(letras_acertadas)