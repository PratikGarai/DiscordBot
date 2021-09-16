class Connect4 :
    def __init__(self) :
        self.ongoing = False
        self.player1 = ""
        self.player2 = ""
        self.turn = 0
    
    def start_game(self, p1, p2) :
        try :
            p1 = p1[3:-1]
            p2 = p2[3:-1]
        except :
            return False
        self.ongoing = True
        self.player1 = p1
        self.player2 = p2
        return True

    def play(self, ctx) :
        self.turn = (self.turn+1)%2