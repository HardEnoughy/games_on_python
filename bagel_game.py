from random import randint

class Bagel:
    def __init__(self):
        self.len_of_num = 3
        self.random_num = []
        self.player_guess = []
        self.hint = []
    
    def check_guess(self):
        for i in range(len(self.random_num)):
            if self.player_guess[i] in self.random_num and self.random_num[i] == self.player_guess[i]:
                self.hint.append('Fermi')
            elif self.player_guess[i] in self.random_num:
                self.hint.append('Pico')
            else:
                self.hint.append('Bagels')
    
    def generate_random_num(self):
        i = 0
        while i < self.len_of_num:
            random_num = randint(1, 9)
            if random_num not in self.random_num:
                self.random_num.append(random_num)
            else:
                continue
            i += 1
    
    def clear_hint(self):
        self.hint = []
    
    def clear_guess(self):
        self.player_guess = []
    
    def clear_random_num(self):
        self.random_num = []
    
    def clear_all(self):
        self.check_guess()
        self.clear_hint()
        self.clear_random_num()
    
    def build_string_hint(self):
        res = ''
        for word in self.hint:
           res += word + ' ' 
        return res
    
    def is_end(self):
        pass

    def restart_game(self):
        self.clear_all()
