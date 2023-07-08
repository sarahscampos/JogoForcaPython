def jogar():
    print('-' * 30)
    print("Bem vindo ao jogo da forca")
    print('-' * 30)

jogar()

palavra_secreta = "caqui".upper()
letras_acertadas = ["_" for letra in palavra_secreta]


enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.strip().upper() # essas funções de string não alteram a string original/ STRINGS SÃO IMUTÁVEIS
    
    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1 
        print("Poxa, você errou! Faltam {} tentativas.".format(6-erros))  

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if(acertou):
    print("Você ganhou!!!")
else:
    print("Você perdeu :( Tente novamente!")