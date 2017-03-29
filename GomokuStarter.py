from Player import Player
from Board import Board

class GomokuStarter:
    def __init__(self):
        self.size=-1
        self._name=""
        self.sign=0

    def Start(self):
        print("Welcome in Gomoku. Let's start a game...\nGood luck!")
        while len(self._name) == 0:
            self._name = input('What is your name?\n')
#        password=input('type your password')
#       correct_password = PasswordValidator
#       while(correct_password.validate):
#       password="Your password is incorrect. Try again:\n")
        try:
            self.size = int(input('{} what board size do you prefer? Choose 3,4,5,6,7,8,9 or 10\n'.format(self._name)))
        except ValueError:
            self.size=0
        while self.size < 2 or self.size > 11:
            print('This size is incorrect. Type again')
            try:
                self.size=int( input('{} what board size do you prefer? Choose 3,4,5,6,7,8,9 or 10\n'.format(self._name)))
            except ValueError:
                self.size=0
        try:
            self.sign = int(input('Would you like to be X or O? If you prefer X type -1, otherwise 1\n'))
        except ValueError:
            self.sign=0
        while self.sign!=-1 and self.sign!=1:
            print("This is incorrect number. Choose again. If you prefer X type -1, otherwise 1")
            try:
                self.sign = int(input('Would you like to be X or O? If you prefer X type -1, otherwise 1\n'))
            except ValueError:
                self.sign=0
        print("Well done. Let's start a game!")
    def return_player(self):
        player = Player(self._name, self.sign,1) # player nr=1
        return player
    def return_board(self):
        board = Board(self.size)
        return board



