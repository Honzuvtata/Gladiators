class Arena:
    playerName = None
    turn = 0
    player1 = None
    player2 = None
    
    def __init__(self, playerName):
        self.playerName = playerName

    def info(self):
        print('Player name: ', self.playerName, 'Turn: ', self.turn)

    def resetTurnCounter(self):
        self.turn = 0
        
    def getPlayer1(self, playerObject):
        self.player1 = playerObject
        
    def getPlayer2(self, playerObject):
        self.player2 = playerObject


        
     
arena = Arena('Player1')