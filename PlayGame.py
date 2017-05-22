from Gomoku import Gomoku
import logging
import os


if __name__=="__main__":
    if os.path.isfile("Logs.log"):
        os.unlink("Logs.log")
    logging.basicConfig(filename="Logs.log", level=logging.INFO)

    logging.info("Player started Gomoku game.")
    new_game = Gomoku()
    new_game.Gomoku()
