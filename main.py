import pygame
from game.game import Game

def main():
  pygame.init()
  pygame.display.set_caption("Snakes and Ladders")

  game = Game()
  game.run()

if __name__ == "__main__":
  main()