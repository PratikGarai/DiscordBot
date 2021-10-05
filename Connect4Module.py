from discord.ext import commands
import numpy as np

class Connect4 :
    def __init__(self) :
        self.ongoing = False
        self.player1 = ""
        self.player2 = ""
        self.id1 = 0
        self.id2 = 0
        self.rows = 6
        self.cols = 7
        self.board = np.zeros((self.rows,self.cols))
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

    async def play(self, ctx:commands.Context, col) :
        if not self.ongoing :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```No game is being played right now```") 
            return
        if ctx.message.author.id not in (self.id1, self.id2) :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```Sorry, you are not a valid player```") 
            return
        if self.turn==0 and ctx.message.author.id!=self.id1 :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```Sorry, not your turn now```") 
            return
        if self.turn==1 and ctx.message.author.id!=self.id2 :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```Sorry, not your turn now```") 
            return
        col = int(col)
        if col<1 or col>self.cols :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```Invalid column, please try again```")
            return 
        row = self.getNextOpenRow(col-1)
        if row==self.rows :
            await ctx.message.add_reaction("🔴")
            await ctx.send("```Column is full right now```")
            return 
        await ctx.message.add_reaction("🟢")
        self.board[row][col-1] = self.turn+1

        tbl = self.show_table()

        if self.winning_move(self.turn+1) :
            if self.turn==0 :
                await ctx.send(f"{tbl}{self.player1} has won!")
            else :
                await ctx.send(f"{tbl}{self.player2} has won!")
            self.ongoing = False
            self.player1 = ""
            self.player2 = ""
            self.id1 = 0
            self.id2 = 0
            self.rows = 6
            self.cols = 7
            self.board = np.zeros((self.rows,self.cols))
            self.turn = 0
            return
        
        self.turn = (self.turn+1)%2
        if self.turn==0 :
            await ctx.send(f"{tbl}{self.player1}'s turn now")
        else :
            await ctx.send(f"{tbl}{self.player2}'s turn now")


    def getNextOpenRow(self, col) :
        for r in range(self.cols):
            if self.board[r][col]==0:
                return r
    
    def winning_move(self, piece):
        # Horizontal check
        for c in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][c]==piece and \
                    self.board[r][c+1]==piece and \
                    self.board[r][c+2]==piece and \
                    self.board[r][c+3]==piece :
                    return True
        
        # Vertical check
        for c in range(self.cols):
            for r in range(self.rows-3):
                if self.board[r][c]==piece and \
                    self.board[r+1][c]==piece and \
                    self.board[r+2][c]==piece and \
                    self.board[r+3][c]==piece :
                    return True
        
        # Top Left to Bottom Right check
        for c in range(self.cols-3):
            for r in range(self.rows-3):
                if self.board[r][c]==piece and \
                    self.board[r+1][c+1]==piece and \
                    self.board[r+2][c+2]==piece and \
                    self.board[r+3][c+3]==piece :
                    return True
        
        # Bottom Left to Top Right check
        for c in range(self.cols-3):
            for r in range(3, self.rows):
                if self.board[r][c]==piece and \
                    self.board[r-1][c+1]==piece and \
                    self.board[r-2][c+2]==piece and \
                    self.board[r-3][c+3]==piece :
                    return True
    
    def show_table(self) :
        msg = "\n```\nBoard state :"
        msg += "\n\n"
        msg += (2*self.cols+1)*"-"+"\n"
        for i in self.board[::-1] :
            msg += "|" 
            for j in i :
                msg += "x|" if j==1 else "o|" if j==2 else " |"
            msg += "\n"
        msg += (2*self.cols+1)*"-"
        msg += "```" 

        return msg