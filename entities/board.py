import pygame
from typing import Iterable
from config import screen_size, tile_amount

from entities.player import Player

class Board:
  def __init__(self):
    self.screen = pygame.display.set_mode((screen_size, screen_size))
    self.board_image = pygame.image.load("data/snakes_and_ladders_board.png")
    self.board_image = pygame.transform.scale(self.board_image, (screen_size, screen_size))
    self.tile_size = screen_size / tile_amount

  def draw_board(self):
    self.screen.blit(self.board_image, (0, 0))

  def get_square_coords(self, position):
    position_index = position - 1
    row = 10 - (position_index // tile_amount)
    col = (position_index % tile_amount) + 1 if row % 2 == 0 else tile_amount - (position_index % tile_amount)
    x = col * self.tile_size - self.tile_size / 2
    y = row * self.tile_size - self.tile_size / 2
    return x, y
  
  def draw_players(self, player_list: Iterable[Player]):
    for i, player in enumerate(player_list):
      x, y = self.get_square_coords(player.position)
      pygame.draw.circle(self.screen, player.color, (x, y), 22)