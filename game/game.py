import pygame
import random
from game.game_state import GameState
from entities.player import Player
from entities.board import Board
from config import dice_size

class Game:
  def __init__(self):
    self.board = Board()
    self.game_state = GameState()
    self.is_running = False
    # self.font = pygame.font.SysFont(None, 30)

  def run(self):
    self.is_running = True

    # Set first player has turn
    self.game_state.get_player_list()[0].set_player_has_turn()
    
    # Render Screen
    self.render_screen()

    while self.is_running:
      self.handle_user_events()

  def handle_user_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.is_running = False
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        self.game_loop()

  def game_loop(self):
    while True:
      # Roll dice
      dice_roll = self.roll_dice()
      # Move player
      self.move_player(self.game_state.get_current_player(), dice_roll)

      if dice_roll != dice_size: break

    # Check for game over
    game_over, winner = self.check_game_over()
    if game_over:
      print(f"\n{winner} wins!")
      self.is_running = False
      pygame.quit()
      return

    # Switch to next player
    self.game_state.pass_turn_to_next_player()
    
    # Render Screen
    self.render_screen()

  def render_screen(self):
    self.board.draw_board()
    self.board.draw_players(self.game_state.get_player_list())
    pygame.display.flip()

  def roll_dice(self):
    roll = random.randint(1, dice_size)
    print(f"{self.game_state.get_current_player().name} rolled a {roll}.")
    return roll

  def move_player(self, current_player: Player, spaces: int):
    new_position = current_player.position + spaces

    # Check if new position is valid
    if new_position > 100:
      return current_player.position

    # Update player position
    current_player.position = new_position

    # Check for ladders and snakes
    if current_player.position in self.game_state.get_ladders():
      current_player.position = self.game_state.get_ladders()[current_player.position]
      print(f"{current_player.name} climbed a ladder to square {current_player.position}.")
    elif current_player.position in self.game_state.get_snakes():
      current_player.position = self.game_state.get_snakes()[current_player.position]
      print(f"{current_player.name} slid down a snake to square {current_player.position}.")

    # Check for another player on the square
    for i, player in enumerate(self.game_state.get_player_list()):
      if player.name is not current_player.name and player.position == current_player.position:
        player.position = player.position - 1
        print(f"{current_player.name} pushed {player.name} to square {player.position}.")

  def check_game_over(self):
    for i, player in enumerate(self.game_state.get_player_list()):
      if player.position == 100:
        return True, player.name
    return False, None
    