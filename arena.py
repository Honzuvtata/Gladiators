class Arena:
    playerName = None
    turn = 0
    
    def __init__(self, playerName):
        self.playerName = playerName

    def info(self):
        print('Player name: ', self.playerName, 'Turn: ', self.turn)

    def resetTurnCounter(self):
        self.turn = 0
        
        
        
arena = Arena('Player1')
arena.info()