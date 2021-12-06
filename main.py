from os import system
import Database
class Player():
    def __init__(self,name:str,symbol:str) -> None:
        self.name = name
        self.symbol = symbol


class Tabuleiro():
    def createMatriz(self):
        matriz = [[0,0,0], [0,0,0], [0,0,0]]
        return matriz
    
    def __init__(self) -> None:
        self.matriz = self.createMatriz()
        print(self.matriz)
        
    def addPosition(self,player:Player,x:int,y:int):
        if( y > len(self.matriz)-1 or x > len(self.matriz[0])-1 ):
            return False
        if(self.matriz[x][y]!=0):
            return False
        self.matriz[x][y] = player.symbol
        return True

    def showMatriz(self):
        for x in range(0,3):
            for y in range(0,3):
                print(f'[{self.matriz[x][y]:^5}]', end="")  
            print()
    
    def checkWin(self,player:Player,x:int,y:int,lose:Player):
        def Message():
            system('cls')
            self.showMatriz()
            Database.Post(player.name,lose.name)
            print(f"Ganhador: {player.name}\nPontos: {str(Database.Get(player.name))}")
            exit(1)
        matriz = self.matriz
        symbol = player.symbol
        
        if(y+1>2 or y+2>2):
            y = 0
        if(x+1>2 or x+2>2):
            x=0
        for i in range(3):
            if(matriz[i][y]==symbol and  matriz[i][y+1]==symbol and matriz[i][y+2]==symbol):
                Message()
            if(matriz[x][i]==symbol and matriz[x+1][i]==symbol and matriz[x+2][i]==symbol):
                Message()
        if(matriz[1][1]==symbol):
            if(matriz[2][2]==symbol and matriz[0][0]==symbol):
                Message()
            if(matriz[0][2]==symbol and matriz[2][0]==symbol):
                Message()
        if(matriz[x][y]==symbol and matriz[x+1][y+1]==symbol and matriz[x+2][y+2]==symbol):
            Message()
        return 0

class Game():
    def __init__(self) -> None:
        self.tabuleiro = Tabuleiro()
        self.players = []
    def addPlayer(self,player:Player):
        self.players.append(player)
    def Start(self):
        contador = 0
        while(1):
            x,y = "",""
            while( not(x.isdigit()) or not(y.isdigit())):
                system('cls')
                self.tabuleiro.showMatriz()
                print(f"Player: {self.players[contador].name}")
                x = input("Digite a Coordenada X: ")
                y = input("Digite a Coordenada Y: ")

            x,y = int(x),int(y)
            if(self.tabuleiro.addPosition(self.players[contador],x,y)):
                self.tabuleiro.checkWin(self.players[contador],x,y,self.players[contador-1])
                contador+=1
            if(contador>1):
                contador = 0
            
game = Game()
game.addPlayer(Player("Bruno","X"))
game.addPlayer(Player("Guilherme","O"))
game.Start()
