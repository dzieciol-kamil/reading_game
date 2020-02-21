from speech.game import Game
from speech.presentation import GamePresentation
from speech.recognition import Recognition

from speech.words import Words


def main():
    game = Game(Recognition(), Words(), GamePresentation())
    game.play_game()

if __name__ == "__main__":
    main()
