class User:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.incorrect = 0
        self.total = 0
    
    def add(self, flag):
        if flag:
            self.correct += 1
        else:
            self.incorrect += 1
        self.total += 1
    
    def display_stat(self):
        print(f"Name: {self.name}")
        print(f"Amount of games played: {self.total}")
        print(f"Wins: {self.correct}")
        print(f"Loses: {self.incorrect}")
    
    def save_stats(self):
        with open('game_stats.txt', 'a') as file_to:
            file_to.write(self.name + '\n')
            file_to.write(str(self.correct) + '\n')
            file_to.write(str(self.incorrect) + '\n')
            file_to.write(str(self.total) + '\n')
    
    def read_stats(self):
        pass

class Hangin_man:
    def __init__(self, word):
        self.pics = [
            """
            +----+
                 |
                 |
                 |
                 |
            ------
            """,
            """
            +----+
            |    |
            0    |
                 |
                 |
            ------
            """,
            """
            +----+
            |    |
            0    |
            |    |
                 |
            ------
            """,
            """
            +----+
            |    |
            0    |
            |\   |
                 |
            ------
            """,
            """
            +----+
            |    |
            0    |
           /|\   |
                 |
            ------
            """,
            """
            +----+
            |    |
            0    |
           /|\   |
           / \   |
            ------
            """,
        ]
        self.word = word
        self.guess = list('_' for i in range(len(word)))

    def display_hangman(self, n):
        if n > 5:
            n = 5
        print(self.pics[n])
    
    def display_text(self, flag):
        if flag:
            print("You guessed correctly")
        else:
            print("Nope, wrong guess")
    
    def display_guess(self):
        print(*self.guess)

    def is_correct(self, letter):
        return letter in self.word and letter not in self.guess
    
    def display_win(self):
        print("You win!")
    
    def display_lose(self):
        print("You lost(")
    
    def is_end(self, n):
        if n > 5:
            n = 5
        return n == 5 or self.word == ''.join(self.guess)
    
    def is_win(self):
        return self.word == ''.join(self.guess)

k = 0
n = 0
name = input("Input you name: ")
user = User(name)
while True:
    if k == 0:
        word = input("enter word to guess(up to 6 letter): ")
        difficulty = int(input("input difficulty, up to 5: "))
        if difficulty > 5 or difficulty <= 0:
            print("wrong difficulty")
            continue
        game = Hangin_man(word)
        k = 1
    game.display_hangman(n)
    game.display_guess()
    guess = input("make your choice: ")
    if len(guess) != 1:
       print('guess should be one letter') 
       continue
    flag = game.is_correct(guess)
    if flag:
        game.guess[game.word.index(guess)] = guess
    else:
        n += difficulty
    game.display_text(flag)
    if game.is_end(n):
        game.display_hangman(n)
        game.display_guess()
        if game.is_win():
            game.display_win()
            user.add(True)
        else:
            game.display_lose()
            user.add(False)
        user.display_stat() 
        again = input("do you want play again? print yes if yes: ")
        if again == 'yes':
            k = 0
            n = 0
        else:
            print("Thanks for playing!")
            user.save_stats()
            break
