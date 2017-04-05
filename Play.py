from random import randint

class Play:
    def __init__(self,board, player0, player1):
        self.board=board
        self.player0=player0
        self.player1=player1

    def play(self, player_nr):
        if player_nr==0:

            position_y=position_x=-1
            while not self.board.is_empty(position_x, position_y):
                position_x = randint(1, self.board.size)
                position_y = randint(1, self.board.size)
            if self.board.set_position(position_x, position_y, self.player0.sign):
                print("Press ENTER to continue")
                while input() != "":
                    pass
                self.board.write_board()
                return True
            else:
                return False
        else:
            print("It's your turn now!")
            try:
                position_x = int(input('Give row position of your choice\n'))
            except ValueError:
                position_x=0
            while position_x < 1 or position_x > self.board.size:
                try:
                    position_x = int(input('Incorrect position number. Give row position of your choice from [0,{}]\n'.format(self.board.size)))
                except ValueError:
                    position_x=0
            try:
                position_y = int(input('Give cloumn position of your choice\n'))
            except ValueError:
                position_y=0
            while position_y < 1 or position_y > self.board.size:
                try:
                    position_y = int(input('Incorrect position number. Give column position of your choice from [0,{}]\n'.format(self.board.size)))
                except ValueError:
                    position_y=0
            if self.board.set_position(position_x, position_y, self.player1.sign):
                self.board.write_board()
                print("Well done. It's computer turn now!")
                return True
            else:
                print("You have chosen not empty position. Choose another one")
                return False
