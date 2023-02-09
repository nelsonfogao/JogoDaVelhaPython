branco = ''
tabuleiro=[
    [branco,branco,branco],
    [branco,branco,branco],
    [branco,branco,branco],
    ]
jogo = True
jogador1 = 'x'
jogador2 = 'o'
jogadas = 0
                        
def imprimeBoard(tabuleiro):
    print(f'{tabuleiro[0]}'+ f'\n{tabuleiro[1]}'+ f'\n{tabuleiro[2]}' )

def verificaJogada(jogador, jogadas):
    jogadorLinha = int(input("escolha a linha onde quer colocar sua jogada: "))
    if(jogadorLinha < 1 or jogadorLinha > 3):
        print("########comando invalido, digite outro numero########")
        return verificaJogada(jogador, jogadas)
    jogadorColuna = int(input("escolha a coluna onde quer colocar sua jogada: "))
    if(jogadorColuna < 1 or jogadorColuna > 3):
        print("########comando invalido, digite outro numero########")
        return verificaJogada(jogador, jogadas)
    else:
        return marcaJogada(jogadorLinha-1, jogadorColuna-1, tabuleiro, jogador, jogadas)
    
def marcaJogada(a, b, tabuleiro, jogador, jogadas):
    if (tabuleiro[a][b] == branco):
        tabuleiro[a][b] = jogador
        return True
    else:
        print('########jogada invalida########')    
         
def verificaVitoria(tabuleiro):
    if  (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != branco):
        return True
    elif  (tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != branco):
        return True
    elif  (tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != branco):
        return True
    
    elif  (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != branco):
        return True
    elif  (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != branco):
        return True
    
    
    elif  (tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != branco):
        return True
    elif  (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != branco):
        return True
    elif  (tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != branco):
        return True
    else:
        return False
    
while(jogo == True):
    imprimeBoard(tabuleiro)
    if(jogadas %2 == 0):
        validaJogada = verificaJogada(jogador1, jogadas)
    else:
        validaJogada = verificaJogada(jogador2, jogadas)
    if(validaJogada == True):
        jogadas = jogadas + 1
    if(verificaVitoria(tabuleiro) == True):
        print('---------fim de jogo---------')
        if(jogadas %2 == 0):
            print('**********vitoria jogador 2**********')
            imprimeBoard(tabuleiro)
            jogo = False
            break
            
        else:
            print('**********vitoria jogador 1**********')
            imprimeBoard(tabuleiro)
            jogo = False
            break
    if (jogadas >= 9):
        print('**********deu velha**********')
        imprimeBoard(tabuleiro)
        jogo = False
    

