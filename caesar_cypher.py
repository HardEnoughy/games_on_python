class Caesar:
    def __init__(self, key, message):
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.message = message
        self.answer = ''
        self.encrypted = ''
        self.key = key

    def encrypt(self):
        for i in range(len(self.message)):
            if message[i] == ' ':
                self.answer += ' '
                continue
            pos = self.key + self.symbols.index(self.message[i])
            if pos >= len(self.symbols):
                while pos >= len(self.symbols):
                    pos -= len(self.symbols)
            self.answer += self.symbols[pos]

    def decrypt(self):
        for i in range(len(self.answer)):
            if self.answer[i] == ' ':
                self.encrypted += ' '
                continue
            pos = self.symbols.index(self.answer[i]) - self.key
            self.encrypted += self.symbols[pos]

    def choose(self, choose):
        if choose in ('encrypt', 'e'):
            self.encrypt()
        elif choose in ('decrypt', 'd'):
            self.decrypt()
        else:
            return -1

message = input('enter your message: ')
key = int(input('enter key: '))
caesar = Caesar(key, message)
caesar.encrypt()
print(caesar.answer)
caesar.decrypt()
print(caesar.encrypted)

