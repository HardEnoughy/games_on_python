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
        print('  12345678')
        print('+----------+')
        for line in self.board:
            print('|', ''.join(line), '|')
        print('+----------+')
        print('  12345678')

    def place_on_map(self, pos, to_place):
        line, column = pos
        self.board[line][column] = to_place

    def scoring(self, pos, side, opposite_side):
        line, column = pos
        if self.board[line][column] != ' ':
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
                        return None
                except:
                    continue
        self.place_on_map(pos, side)

game = Reversegam(1, 2)
game.fill_board()
game.draw_map()
game.scoring((4, 2), 'X', 'O')
game.draw_map()

