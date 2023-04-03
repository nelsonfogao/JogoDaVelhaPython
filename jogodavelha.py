def VerificaTabuleiro(tabuleiro):
    print("Tabuleiro : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(tabuleiro[i]==0):
            print("- ",end=" ");
        if (tabuleiro[i]==1):
            print("O ",end=" ");
        if(tabuleiro[i]==-1):    
            print("X ",end=" ");
    print("\n\n");


def TurnoJogador1(tabuleiro):
    pos=input("Digite uma posicao de [1...9]: ");
    pos=int(pos);
    if(tabuleiro[pos-1]!=0):
        print("Jogada Invalida!!!");
        exit(0) ;
    tabuleiro[pos-1]=-1;


def Minimax(tabuleiro,jogador):
    x=verificaTabuleiro(tabuleiro);
    if(x!=0):
        return (x*jogador);
    pos=-1;
    valor=-2;
    for i in range(0,9):
        if(tabuleiro[i]==0):
            tabuleiro[i]=jogador;
            total=-Minimax(tabuleiro,(jogador*-1));
            if(total>valor):
                valor=total;
                pos=i;
            tabuleiro[i]=0;

    if(pos==-1):
        return 0;
    return valor;
    

def TurnoPC(tabuleiro):
    pos=-1;
    valor=-2;
    for i in range(0,9):
        if(tabuleiro[i]==0):
            tabuleiro[i]=1;
            total=-Minimax(tabuleiro, -1);
            tabuleiro[i]=0;
            if(total>valor):
                valor=total;
                pos=i;
 
    tabuleiro[pos]=1;



def verificaTabuleiro(tabuleiro):
    t=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(tabuleiro[t[i][0]] != 0 and
           tabuleiro[t[i][0]] == tabuleiro[t[i][1]] and
           tabuleiro[t[i][0]] == tabuleiro[t[i][2]]):
            return tabuleiro[t[i][2]];
    return 0;

def main():
    tabuleiro=[0,0,0,0,0,0,0,0,0];
    jogador = 1;
    for i in range (0,9):
        if(verificaTabuleiro(tabuleiro)!=0):
            break;
        if((i+jogador)%2==0):
            TurnoPC(tabuleiro);
        else:
            VerificaTabuleiro(tabuleiro);
            TurnoJogador1(tabuleiro);
         

    x=verificaTabuleiro(tabuleiro);
    if(x==0):
         VerificaTabuleiro(tabuleiro);
         print("Deu Velha!!!")
    if(x==-1):
         VerificaTabuleiro(tabuleiro);
         print("X Ganhou!!!")
    if(x==1):
         VerificaTabuleiro(tabuleiro);
         print("O Wins !!!!")
       

main()