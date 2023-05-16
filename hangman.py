from random import choice
# Importa a biblioteca random para gerar números aleatórios
#o choice() é um método da biblioteca random que escolhe um elemento aleatório de uma lista
vaissubstituido = ["esquistossomose", "naftalina", "ribonucleico", "idiossincratico", "fagocitose", "quinquagesimo"]

def cabecalho():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    print("Você tem 5 tentativas para acertar a palavra secreta!\n")
    
def numero_jogadores():
    while True:
        num_jogadores= int(input("Quantos jogadores vão jogar? 1 ou 2? "))
        if num_jogadores in [1,2]:
            return int(num_jogadores)
        else:
            print("Escolha 1 ou 2")
            continue
def nome_jogador(jogador_numero):
    nome_jogador = input(f"Qual sera o nome do jogador {jogador_numero}? ")
    return nome_jogador   
   
def secreto():
    palavra = choice(vaissubstituido)
    palavra = palavra.upper() #deixa a palavra em maiúsculo
    return palavra #retorna a palavra secreta

def tracos(palavra):
    for letra in palavra:
	    print('_', end= ' ')
    print()
    
def main():
    cabecalho()
    num_jogadores = numero_jogadores()
    nome_jogadores = [nome_jogador(i+1) for i in range(num_jogadores)]
    palavra_secreta = secreto()
    print(f"Você tem 5 tentativas para acertar a palavra secreta!\n")
    tracos(palavra_secreta)

# Executa o jogo
if __name__ == "__main__":
    main()






