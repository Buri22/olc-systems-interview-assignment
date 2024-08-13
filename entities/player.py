from utils.utils import get_random_color

class Player:
  def __init__(self, name):
    self.name = name
    self.color = get_random_color()
    self.position = 1
    self.is_my_turn = False

  def set_player_has_turn(self):
    self.is_my_turn = True