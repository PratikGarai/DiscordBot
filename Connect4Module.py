class Connect4 :
    def __init__(self) :
        self.ongoing = False
        self.player1 = ""
        self.player2 = ""
        self.id1 = 0
        self.id2 = 0
        self.turn = 0
    
    def start_game(self, p1, p2) :
        if p1==p2 :
            return False
        try :
            c1 = int(p1[3:-1])
            c2 = int(p2[3:-1])
        except :
            return False
        self.ongoing = True
        self.player1 = p1
        self.player2 = p2
        self.id1 = c1
        self.id2 = c2
        return True

    def play(self, ctx) :
        self.turn = (self.turn+1)%2