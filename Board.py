
class Board:
    def __init__(self, size=0):
        self.size = size
        self.board = []
        for i in range(0,self.size):
            self.board.append([])
            for j in range(0, self.size):
                self.board[i].append(0)
    def is_empty(self, x, y):
        if self.board[y-1][x-1]==0:
            return True
        else:
            return False
    def set_position(self, x, y, sign):
        if self.board[x-1][y-1]==0:
            self.board[x-1][y-1]=sign
            return True
        else:
            return False

    def write_board(self):
        string="  "
        for i in range(0,self.size):
            string+=str(i+1)
            string+=" "
        print(string)
        for i in range(0,self.size):
            string = str(i+1)
            string += "|"
            for j in range (0,self.size):
                if self.board[i][j]==1:
                    string+="O"
                elif self.board[i][j]==-1:
                    string+="X"
                else:
                    string+="_"
                string+='|'
            print(string)
 #       print(string_pauza)












