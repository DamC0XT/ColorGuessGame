import random




class ColorGame:
    userScore = 0
    computerScore = 0
    def __init__(self):
        self.colors = ["red","blue","green","yellow","orange"]
        self.choice = 0
        self.computer = 0




    def getUserInput(self,choice):


        self.choice = choice
        userChoice = 0
        if self.choice == '0':
            userChoice = 0
        elif self.choice == '1':
            userChoice = 1
        elif self.choice == '2':
            userChoice = 2
        elif self.choice == '3':
            userChoice = 3
        elif self.choice == '4':
            userChoice = 4



        userString = "Player Selected " + str(self.colors[userChoice])
        return userString

    def computerTurn(self):

        computerChoice = random.randint(0,4)
        self.computer = computerChoice
        compString = "Computer Selected " + str(self.colors[computerChoice])
        return compString


    def gameWelcome(self):
        myString = str("Welcome to the Color Choice Game") + "\n" + str("The Color Choice Are: ") + "\n" + str("red = 0") + "\n" + str("blue = 1") + \
                   "\n" + str("green = 2") + "\n" + str("yellow = 3") + "\n" + str("orange = 4")

        return myString

    def Score(self):
        userChoice = 0
        if self.choice == '0':
            userChoice = 0
        elif self.choice == '1':
            userChoice = 1
        elif self.choice == '2':
            userChoice = 2
        elif self.choice == '3':
            userChoice = 3
        elif self.choice == '4':
            userChoice = 4

        if self.colors[userChoice] == self.colors[self.computer]:

            self.userScore +=1
        else:
            self.computerScore +=1

        return self.userScore,self.computerScore


    def winner(self,user,computer):
        winner = ""
        if user < computer:
            winner = "Computer Wins"
        elif user > computer:
            winner = "Player Wins"
        else:
            winner = "The Game is a Draw"
        return winner












