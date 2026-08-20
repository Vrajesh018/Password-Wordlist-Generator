import random

class passList:
    def __init__(self):
        """ Consttuctor for the class to initialize variables & start program."""
        self.wordLst = []
        self.specialChar = "\"#^*_+-=~`\\|:;',./!@$%&(){}[]<>?"
        self.infoValue = {
            1 : "Name only",
            2 : "Name & DOB",
            3 : "Name, DOB & Account name"
        }
        self.exit = False


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
          

if __name__ == "__main__":
    try:
        while True:
            target = passList()
            target.Welcome()
            target.Target_Info()
    except KeyboardInterrupt:
        print("\n\n\t\t Program Interrupted...\n")