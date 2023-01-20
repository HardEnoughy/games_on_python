class Caesar:
    def __init__(self, message):
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.message = message
        self.answer = ''
        self.encrypted = ''

    def encrypt(self, key):
        for i in range(len(self.message)):
            if message[i] == ' ':
                self.answer += ' '
                continue
            pos = key + self.symbols.index(self.message[i])
            if pos >= len(self.symbols):
                while pos >= len(self.symbols):
                    pos -= len(self.symbols)
            self.answer += self.symbols[pos]

    def decrypt(self, key):
        for i in range(len(self.answer)):
            if self.answer[i] == ' ':
                self.encrypted += ' '
                continue
            pos = self.symbols.index(self.answer[i]) - key
            if pos <= -len(self.symbols):
                while pos <= -len(self.symbols):
                    pos += len(self.symbols)
            self.encrypted += self.symbols[pos]

    def choose(self, choose):
        if choose in ('encrypt', 'e'):
            self.encrypt()
        elif choose in ('decrypt', 'd'):
            self.decrypt()
        else:
            return -1

    def brute_decrypt(self):
        for i in range(1, len(self.message)):
            self.encrypted = ''
            self.decrypt(i)
            print(self.encrypted)

message = input('enter your message: ')
key = int(input('enter key: '))
caesar = Caesar(message)
caesar.encrypt(key)
print(caesar.answer)
caesar.brute_decrypt()

