from random import randint
import math

class SonarTreasureHunt:
    def __init__(self):
        self.map = []
        self.chests_pos = []
        self.sonar_pos = []
        self.num_of_try = 20

    def create_map(self):
        for y in range(15):
            self.map.append([])
            for x in range(60):
                if randint(0, 1) == 0:
                    self.map[y].append('~')
                else:
                    self.map[y].append('`')

    def draw_map(self):
        print(' ', '0123456789' * 6)
        for i in range(15):
            line = f"{i} {''.join(self.map[i])} {i}"
            print(line)
        print(' ', '0123456789' * 6)

    def random_chest_pos(self):
        x_pos = randint(0, 59)
        y_pos = randint(0, 14)
        self.chests_pos.append((x_pos, y_pos))

    def found_chest(self, pos):
        x, y = pos
        self.chests_pos.remove(self.chests_pos[x])
        self.remove_hints(pos)

    def calculate_hint(self, guess):
        self.sonar_pos.append(guess)
        mini = 1000
        for chest in self.chests_pos:
            calc = abs(sum(chest) - sum(guess))
            if calc == 0:
                self.found_chest(guess)
                return -1
            if calc < mini:
                mini = calc
        return mini

    def place_on_map(self, coord, to_place):
        x, y = coord
        self.map[x][y] = str(to_place)

    def remove_hints(self, pos_of_chest):
        self.place_on_map(pos_of_chest, 'X')
        for pos in self.sonar_pos:
            self.place_on_map(pos, 'X')

    def clear_map(self):
        self.map = []

    def is_end(self):
        if not self.chests_pos:
            self.win()
            return True
        elif self.num_of_try == 0:
            self.lose()
            return True
        return False

    def win(self):
        print("You won! Congrats!")

    def lose(self):
        print("You lost( You will be more lucky next time!")

    def try_again(self):
        inp = input("Do you want to try again? Input yes")
        return inp == 'yes'
    
    def restart(self):
        pass


game = SonarTreasureHunt()
game.create_map()
for i in range(3):
    game.random_chest_pos()
while True:
    game.draw_map()
    pos = list(map(int, input("input you guess here: ").split()))
    hint = game.calculate_hint(pos)
    game.num_of_try -= 1
    if hint == -1:
        print("you found chest, congrats!")
    else:
        game.place_on_map(pos, hint)
        print(f"you got closer to chest. You have {game.num_of_try}")
    if game.is_end():
        if game.try_again():
            game.restart()
        else:
            break

