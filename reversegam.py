class Reversegam:
    def __init__(self, player, computer):
        self.board = []
        self.computer_side = computer
        self.player_side = player
        self.computer_score = 0
        self.player_score = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def fill_board(self):
        self.board = []
        for i in range(8):
            self.board.append([' ' for i in range(8)])
        self.board[3][3] = 'X'
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'
        self.board[4][4] = 'X'

    def draw_map(self):
        print('  01234567')
        print('+----------+')
        for line in self.board:
            print('|', ''.join(line), '|')
        print('+----------+')
        print('  01234567')

    def place_on_map(self, pos, to_place):
        line, column = pos
        self.board[line][column] = to_place

    def scoring(self, pos, side, opposite_side):
        line, column = pos
        flag = False
        if not self.is_valid_move(pos):
            return False
        for i in self.directions:
            new_pos = (i[0] + line, i[1] + column)
            if self.board[new_pos[0]][new_pos[1]] == opposite_side:
                try:
                    if self.board[new_pos[0] + i[0]][new_pos[1] + i[1]] == side:
                        self.place_on_map(new_pos, side)
                        self.place_on_map(pos, side)
                        if side == self.player_side:
                            self.player_score += 1
                        else:
                            self.computer_score += 1
                        flag = True
                except:
                    continue
        if not flag:
            self.place_on_map(pos, side)

    def most_score(self, pos):
        score = 0
        line, column = pos
        for i in self.directions:
            try:
                new_pos = (i[0] + line, i[1] + column)
                if self.board[new_pos[0]][new_pos[1]] == self.player_side:
                 try:
                     if self.board[new_pos[0] + i[0]][new_pos[1] + i[1]] == self.computer_side:
                         score += 1
                 except:
                     continue
            except:
                continue
        return score

    def check_every_move(self):
        maxi = 0
        res_pos = ()
        for line in range(len(self.board)):
            for column in range(len(self.board)):
                if self.is_valid_move((line, column)):
                    res = self.most_score((line, column))
                    if res > maxi:
                        maxi = res
                        res_pos = (line, column)
        self.scoring(res_pos, self.computer_side, self.player_side)

    def is_valid_move(self, pos):
        line, column = pos
        return self.board[line][column] == ' '

    def take_corner(self):
        pass

    def decide(self):
        pass

    def is_end(self):
        for line in self.board:
            if ' ' in line:
                return False
        return True

    def who_won(self):
        return 'computer' if self.computer_score > self.player_score else 'player'

game = Reversegam('X', 'O')
game.fill_board()
while True:
    game.draw_map()
    pos = list(map(int, input("make your move: ").split()))
    game.scoring(pos, 'X', 'O')
    game.draw_map()
    game.check_every_move()
    if game.is_end():
        game.draw_map()
        break

