from random import randint

class Tic_tac_toe:
    def __init__(self, player_side, computer_side):
      #board settings
        self.controls = {
          1: ' ', 
          2: ' ', 
          3: ' ',  
          4: ' ',  
          5: ' ',  
          6: ' ', 
          7: ' ',
          8: ' ',
          9: ' ',
        }
        self.board = [
          [7, 8, 9],
          [4, 5, 6],
          [1, 2, 3],
          [7, 5, 3],
          [1, 5, 9],
          [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]
        ]
        self.pics = f"""
            ___________________________________________________________________
            |                     |                     |                     |
            |          {self.controls[7]}          |          {self.controls[8]}          |          {self.controls[9]}          |
          __|_____________________|_____________________|_____________________|
            |                     |                     |                     | 
            |          {self.controls[4]}          |          {self.controls[5]}          |          {self.controls[6]}          |
          __|_____________________|_____________________|_____________________|
            |                     |                     |                     | 
            |          {self.controls[1]}          |          {self.controls[2]}          |          {self.controls[3]}          |
          __|_____________________|_____________________|_____________________|
        """

        #player and computer settings
        self.player_side = player_side
        self.computer_side = computer_side
        self.player_moves = []
        self.computer_moves = []

    def player_move(self, move):
      if self.controls[move] == ' ':
        self.controls[move] = self.player_side
        self.player_moves.append(move)
        return True
      else:
        return False
    
    def update_board(self):
      self.pics = f"""
            ___________________________________________________________________
            |                     |                     |                     |
            |          {self.controls[7]}          |          {self.controls[8]}          |          {self.controls[9]}          |
          __|_____________________|_____________________|_____________________|
            |                     |                     |                     | 
            |          {self.controls[4]}          |          {self.controls[5]}          |          {self.controls[6]}          |
          __|_____________________|_____________________|_____________________|
            |                     |                     |                     | 
            |          {self.controls[1]}          |          {self.controls[2]}          |          {self.controls[3]}          |
          __|_____________________|_____________________|_____________________|
        """
    
    def find_player_neighbour(self):
      dirs = [-2, 2, 1, -1, 4, -4, 3, -3]
      for dirr in dirs:
        res = self.player_last_move + dirr
        if res > 0 and res < 10 and self.controls[res] == self.player_side:
          return res 
    
    def find_pos(self):
      for i in self.board:
        try:
          if self.player_moves[-1] in i and self.player_moves[-2] in i:
            return sum(i) - (self.player_moves[-1] + self.player_moves[-2])
        except:
          return False
      return False

    def prevent_win(self):
      pos = self.find_pos()
      if self.controls[pos] == ' ':
        self.controls[pos] = self.computer_side
        self.computer_moves.append(pos)
    
    def ai_attack(self):
      while True:
        random_pos = randint(1, 9)
        if self.controls[random_pos] == ' ':
          self.controls[random_pos] = self.computer_side
          self.computer_moves.append(random_pos)
          break

    def clear_board(self):
      self.controls = {
        1: ' ', 
        2: ' ', 
        3: ' ',  
        4: ' ',  
        5: ' ',  
        6: ' ', 
        7: ' ',
        8: ' ',
        9: ' ',
      }
    
    def computer_action(self):
      if self.find_pos():
        self.prevent_win()
      else:
        self.ai_attack()
    
    def is_end(self):
      if self.is_win(self.computer_moves):
        return "computer"
      elif self.is_win(self.player_moves):
        return "player"
      elif self.is_draw():
        return "draw"

    def is_win(self, side):
      for i in self.board:
        if set(i).issubset(side):
          return True
      return False
    
    def is_draw(self):
      for i in self.controls.values():
        if i == ' ':
          return False
      return True
    
    def restart_game(self):
      self.player_moves = []
      self.computer_moves = []
      for key in self.controls.keys():
        self.controls[key] = ' '
      self.update_board()
    
    def play_again(self, choice):
      if choice == 'yes':
        self.restart_game()

game = Tic_tac_toe('X', 'O')
while True:
  choice = input()
  if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
    break
  game.player_move(int(choice))
  game.computer_action()
  game.update_board()
  print(game.pics)
  end = game.is_end()
  if end == "computer":
    print("computer wins!")
    game.play_again(input("do you want play again? "))
  elif end == "player":
    print("player wins")
    game.play_again(input("do you want play again? "))
  elif end == "draw":
    print("this is a draw")
    game.play_again(input("do you want play again? "))
