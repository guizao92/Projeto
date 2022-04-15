"""
Desafio Labirinto Codigo[s]
Guilherme Felipe Pacheco Braga
"""

from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "."
ROBO = "X"
SAIDA = "S"

DIREITA  = [0, 1]
BAIXO    = [1, 0]
ESQUERDA = [0, -1]
CIMA     = [-1, 0]


LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    
def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    nova_posicao = LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]]

    if nova_posicao == PAREDE:
        return False
    elif nova_posicao == CAMINHO_PERCORRIDO:
        return False
    elif nova_posicao == CAMINHO_LIVRE:
        return True
    elif nova_posicao == SAIDA:
        return True

def main():
    
    cond = False

    while cond == False:
        posicao = list(map(int, input("Digite uma linha de 0 a 9 e uma coluna de 0 a 19 para a posição inicial do robô separados por vírgula: ").split(",")))
        if (posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 19):
            posicao = list(map(int, input("Digite uma linha de 0 a 9 e uma coluna de 0 a 19 para a posição inicial do robô separados por vírgula: ").split(",")))
            cond = False
        else:
            if (LABIRINTO[posicao[0]][posicao[1]]) == PAREDE or (LABIRINTO[posicao[0]][posicao[1]] == SAIDA):
                cond = False
            else:
                cond = True
                
    POSICAO_INICIAL = posicao
    
    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    pilha = [posicao]
    tentativa = 0
    pos_saida = [9,18]

    print_labirinto()

    POSICAO_ATUAL = posicao

    while POSICAO_ATUAL != pos_saida:
        direcoes = [DIREITA, ESQUERDA, CIMA, BAIXO]
        for direct in direcoes:
            tentativa = tentativa + 1
            if verifica_movimento(POSICAO_ATUAL, direct):
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, direct)
                pilha.append(POSICAO_ATUAL)
                print_labirinto()
                sleep(0.4)
                tentativa = 0
                
            
            if tentativa > 3:
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = CAMINHO_PERCORRIDO
                pilha.pop()
                POSICAO_ATUAL = pilha[-1]
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
                print_labirinto()
                sleep(0.4)  
                tentativa = 0

    print("*"*40)
    print("\n      PARABÉNS VOCÊ ACHOU A SAÍDA!      \n")
    print("*"*40)
        

if __name__ == "__main__":
    main()