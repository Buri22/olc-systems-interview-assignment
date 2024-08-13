import sys
from entities.player import Player

class GameState:
  def __init__(self):
    self.ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
    self.snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
    self.setup_num_players()
    self.player_list = [Player(f"Player {i+1}") for i in range(self.num_players)]
    self.current_player_index = 0

  def get_player_list(self):
    return self.player_list
  
  def is_num_players_valid(self):
    return self.num_players.is_integer() and self.num_players > 1

  def setup_num_players(self):
    # Get number of players
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
      num_players = int(sys.argv[1])
    else:
      num_players = int(input("Enter the number of players: "))

    self.num_players = num_players
    print(f"Setting num_players to: {self.num_players}")

    while not self.is_num_players_valid():
      self.setup_num_players()

  def get_ladders(self):
    return self.ladders

  def get_snakes(self):
    return self.snakes

  def get_current_player(self):
    return self.player_list[self.current_player_index]
    
  def pass_turn_to_next_player(self):
    self.current_player_index = (self.current_player_index + 1) % self.num_players
    