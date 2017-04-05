
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
            self.is_winner()
            return True
        else:
            return False
    def is_winner(self):
        size=self.size;
        if self.size>5:
            size=5
        sum=0
        for x in range(0, self.size):
            for y in range(0, self.size):
                sum = sum + self.board[x][y]
                if(sum==size or sum==-size ):
                    self.write_board()
                    if(sum<0):
                        print("Game over. The winner is X owner")
                    else:
                        print("Game over. The winner is O owner")
                    exit("Let's play again")
            sum=0
        sum=0
        if (self.size < 6):
            for i in range(0, self.size):
                sum = sum + self.board[i][i]
                if (sum == size or sum==-size ):
                    self.write_board()
                    if (sum < 0):
                        print("Game over. The winner is X owner")
                    else:
                        print("Game over. The winner is O owner")
                    exit("Let's play again")
            sum=0
            iterator=self.size-1
            for x in range(0, self.size):
                sum = sum + self.board[x][iterator]
                iterator=iterator-1
                if (sum == size or sum==-size ):
                    self.write_board()
                    if (sum < 0):
                        print("Game over. The winner is X owner")
                    else:
                        print("Game over. The winner is O owner")
                    exit("Let's play again")
        """else:
            if (self.size < 6):
                for i in range(0, size):
                    sum += self.board[i][i]
                    if (sum == size):
                        if (sum < 0):
                            print("Game over. The winner is X owner")
                        else:
                            print("Game over. The winner is O owner")
                        exit(-1)
                sum = 0
                iterator = size
                for x in range(0, self.size):
                    sum += self.board[x][iterator]
                    iterator = iterator - 1
                    if (sum == size):
                        if (sum < 0):
                            print("Game over. The winner is X owner")
                        else:
                            print("Game over. The winner is O owner")
                        exit(-1)
        """

        sum=0
        for x in range(0, self.size):
            for y in range(0, self.size):
                sum = sum + self.board[x][y]
                if(sum==size or sum==-size ):
                    self.write_board()
                    if (sum < 0):
                        print("Game over. The winner is X owner")
                    else:
                        print("Game over. The winner is O owner")
                    exit("Let's play again")
            sum=0

        sum = 0
        for y in range(0, self.size):
            for x in range(0, self.size):
                sum = sum + self.board[x][y]
                if (sum == size or sum==-size ):
                    self.write_board()
                    if (sum < 0):
                        print("Game over. The winner is X owner")
                    else:
                        print("Game over. The winner is O owner")
                    exit("Let's play again :)")
            sum = 0

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
 











