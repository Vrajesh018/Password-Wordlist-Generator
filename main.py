import random

class passList:
    def __init__(self):
        """ Consttuctor for the class to initialize variables & start program."""
        self.wordLst = []
        self.specialChar = "\"#^*_+-=~`\\|:;',./!@$%&(){}[]<>?"
        self.exit = False
        self.infoValue = {
            1 : "Name only",
            2 : "Name & DOB",
            3 : "Name, DOB & Account name"
        }
                
        self.CommonSubstitutes = {
            "a": ["4", "@"],
            "b": ["8"],
            "c": ["("],
            "d": ["0"],
            "e": ["3", "€"],
            "f": ["ph"],
            "g": ["6", "9", "&"],
            "h": ["#", "4"],
            "i": ["1", "!"],
            "j": ["]"],
            "k": ["X"],
            "l": ["1", "7", "£"],
            "m": ["nn"],
            "n": ["/V"],
            "o": ["0"],
            "p": ["9"],
            "q": ["9"],
            "r": ["2"],
            "s": ["5", "$", "z"],
            "t": ["7", "+"],
            "u": ["v"],
            "v": ["\\/"],
            "w": ["vv"],
            "x": ["%"],
            "y": ["j"],
            "z": ["2"]
        }
    
        self.advSubstitute = {
            "a": ["4", "@", "/\\", "^"],
            "b": ["8", "13", "|3"],
            "c": ["(", "<", "[", "{"],
            "d": ["|)", "])", "0"],
            "e": ["3", "€"],
            "f": ["ph", "ƒ"],
            "g": ["6", "9", "&"],
            "h": ["#", "|-|", "4"],
            "i": ["1", "!", "|"],
            "j": ["_|", "_/", "]"],
            "k": ["|<", "|{", "X"],
            "l": ["1", "7", "|_", "£"],
            "m": ["^^", "/\\/\\", "|\\/|"],
            "n": ["|\\|", "/\\/"],
            "o": ["0", "()", "<>"],
            "p": ["9", "|*", "|o"],
            "q": ["0_", "9", "O_"],
            "r": ["2", "Я", "|2"],
            "s": ["5", "$", "z"],
            "t": ["7", "+", "†"],
            "u": ["(_", "|_|", "v"],
            "v": ["\\/", "\\|/"],
            "w": ["\\/\\/", "vv", "2u"],
            "x": ["%", "><", "}{"],
            "y": ["¥", "j", "'/"],
            "z": ["2", "7_", "-/_"]
        }


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
        print("\n How Much information do you have?\n")
        for i in self.infoValue:
            print(f"{i}. {self.infoValue[i]}")
        while True:
            try:
                self.Info_Num = int(input("\nEnter Value number : "))
                if self.Info_Num > 3:
                    print("Enter valid option number...")
                    continue
            except ValueError:
                print("Enter valid option number...")
                continue
            else:
                break

    def Target_Info(self):
        def name():
            while True:
                user_input = input("Please enter your name : ")
                if not user_input.isalpha():
                    print("\n\t Enter Valid Name!\n")
                else:
                    return user_input
        def DOB():
            while True:
                user_input = input("please enter your DOB in YYYYMMDD format : ")
                if not user_input.isdigit():
                    print("\n\t Enter Valid Date of Birth in YYYYMMDD format!")
                elif len(user_input) != 8:
                    print("\n\t Enter Valid Date of Birth in YYYYMMDD format!")
                    continue
                else:
                    return user_input
        def accName_input():
            while True:
                user_input = input("Please enter Account Name :")
                if user_input.strip():
                    return user_input
 
        self.targetName = name()

        if self.Info_Num >= 2:
            self.targetDOB = DOB()

        if self.Info_Num >= 3:
            self.accName = accName_input()

    def Generator(self):
        nameLength = len(self.targetName)

        subs_wish = input("Do you want to use extended swaps? [y|n] : ")
        def singleSwap():
            with open(f"wordlists\{self.targetName}_Wordlist.txt", "a", encoding="utf-8") as wFile:
                wFile.write(f"{self.targetName}\n")
                for i in range(nameLength):
                    temp = self.targetName
                    swapLetter = self.advSubstitute[self.targetName[i]] if subs_wish == "y" else self.CommonSubstitutes[self.targetName[i]]
                    for j in range(len(swapLetter)):
                        temp = temp[:i] + swapLetter[j] + temp[i + 1 :]
                        wFile.write(f"{temp}\n")

        singleSwap()

    
if __name__ == "__main__":
    try:
        while True:
            target = passList()
            target.Welcome()
            target.Target_Info()
            target.Generator()
            break
    except KeyboardInterrupt:
        print("\n\n\t\t Program Interrupted...\n")