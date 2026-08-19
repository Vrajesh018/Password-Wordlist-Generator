import random

class passList:
    def __init__(self):
        """ Consttuctor for the class to initialize variables & start program."""
        self.wordLst = []
        self.specialChar = "\"#^*_+-=~`\\|:;',./!@$%&(){}[]<>?"


    def Welcome(self):
        """ Welcome page of the program which changes with every time."""
        col = 25
        row = 6
        pattern = self.specialChar[random.randint(0,17)]
        for i in range(row):
            if i == 3:
                print(f"{pattern}\t Password Wordlist Generator! \t\t{pattern}")
            for j in range(col):
        
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    print(pattern, end=" ")
                else:
                    print(" ", end=" ")
            print()


if __name__ == "__main__":
    target = passList()
    target.Welcome()