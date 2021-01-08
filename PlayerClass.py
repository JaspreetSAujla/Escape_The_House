import time

class Player:
    """
    This class will define the player object.
    It will store the essential objects the player needs to escape.
    It will have methods to interact with the essential objects.

    Methods:
        __init__ = Sets the initial variables when the person object is created.

        Bath = Runs the method for when the player interacts with the bath.

        Generator = Runs the code for when the player interacts with the generator.

        Safe = Runs the code for when the player interacts with the safe.

        Nightstand = Runs the code for when the player interacts with the nightstand.

        Desk = Runs the code for when the player interacts with the desk.
    """

    def __init__(self):
        """
        This method defines the initial variables when the person object is created.

        Variables:
            self.escaped = This will track whether the player is allowed to escape or not.
                           All the essential tasks need to be completed to escape.
                           Set to False by default.

            self.power = This will check whether the player has turned on the power.
                         Power needs to be turned on for value to become True.
                         Set to False by default.
            
            self.batteries = Checks whether the player has picked up the batteries.
                             Batteries can be used in the radio.
                             Set to False by default.
            
            self.power_pack = Checks whether the player has picked up the power pack.
                              Power pack used to turn power back on.
                              Set to False by default.
            
            self.token = Checks whether the player has picked up the token to open the
                         washing machine.
                         Set to False by default.

            self.small_key = Checks whether the player has picked up the small key 
                             to open the chest in the attic.
                             Set to False by defualt.
            
            self.big_key = Checks whether the player has picked up the big key
                           to open the front door and escape.
                           Set to False by default.
        """
        self.escaped = False
        self.power = False
        self.batteries = False
        self.power_pack = False
        self.token = False
        self.small_key = False
        self.big_key = False
    


    def Bath(self):
        """
        Runs the code for when the player interacts with the bath.
        If the player does not have the power pack already,
        then they can pick it up.
        Otherwise the bath will be empty.
        """
        # Use if statement to check if player has picked up the power pack already.
        if self.power_pack == False:
            print("There seems to be something in the bath.")
            time.sleep(3)
            print("You find a power pack; this could be useful later.")
            self.power_pack = True
            time.sleep(3)
        else:
            print("There is nothing in the bath.")
            time.sleep(3)
    


    def Generator(self):
        """
        Runs the code for when the player interacts with the generator.
        If the player has the power pack, they will be able to turn on the power.
        If not, the power will remain off.
        If the power is already on, it will stay on.
        """
        # If statment to check if the player has the power pack.
        if self.power_pack == False:
            print("The power will not turn on.")
            time.sleep(3)
            print("It seems like it is missing a power pack.")
            time.sleep(3)
        # Checks if the power is already on.
        elif self.power == True:
            print("The power is already on.")
            time.sleep(3)
        else:
            print("You have a power pack.")
            time.sleep(3)
            print("You place the power pack into the generator.")
            time.sleep(3)
            print("You hear some noise and the power turns on.")
            self.power = True
            time.sleep(3)
    


    def Safe(self):
        """
        Runs the code for when the player interacts with the safe.
        The player has to input the correct password to open the safe.
        The safe contains the small key to open the chest in the attic.

        Variables:
            code_guess = Contains the players guess for the code.
                         Set to None by default.

            try_again = Checks if the player wants to keep guessing or not.
                        Set to True by default.
            
            response = Checks what the response is for the player wanting to try again.
                       Set to None by default.
        """
        code_guess = None
        try_again = True
        response = None

        print("You look at the safe.")
        time.sleep(3)
        print("You see that it needs a 6-digit code to unlock.")
        time.sleep(3)

        # While loop to see if the player wants to keep guessing.
        while try_again == True:
            code_guess = input("What is your guess? \n")
            # Ensure the input is a string.
            code_guess = str(code_guess)
            # Check if the guess is correct.
            if code_guess == "247274":
                print("That is the correct code.")
                time.sleep(3)
                print("The safe opens...")
                time.sleep(3)
                # Checks if the player already has the key or not.
                if self.small_key == True:
                    print("The safe is empty.")
                    time.sleep(3)
                else:
                    print("You look inside and find a small key.")
                    time.sleep(3)
                    print("This looks like it could be used for the front door.")
                    time.sleep(3)
                    print("Or something else maybe...")
                    self.small_key = True
                    time.sleep(3)
                try_again = False
            else:
                print("That is the incorrect code.")
                time.sleep(3)
                print("Would you like to try again?")
                response = input("(yes/no) \n")
                if response == "No" or response == "no":
                    try_again = False



    def Nightstand(self):
        """
        Runs the code for when the player interats with the nightstand.
        The player can read the note or open the drawers.

        Variables:
            response = Allows the player to interact with the nightstand
                       as many times as they like.
                       Set to None by default.
        """
        response = None
        print("You look at the nightstand and see a note on top of it.")
        time.sleep(3)
        print("The nightstand also has 4 drawers.")
        time.sleep(3)

        # While loop to allow player to interact with nightstand as long as they want.
        while response != "Explore" and response != "explore":
            print("What do you do?")
            time.sleep(3)
            print("Read the note, open 1 of the 4 drawers or continue exploring?")
            response = input("(Note/One/Two/Three/Four/Explore) \n")
            if response == "Note" or response == "note":
                print("You pick up the note and read it.")
                time.sleep(3)
                print("It reads:")
                time.sleep(3)
                print("'She is in the house")
                print("Leave while you can")
                print("I did not want to do this to her...'")
                time.sleep(3)
                print("You put the note down.")
                time.sleep(3)
            elif response == "One" or response == "one" or response == "Three" or response == "three":
                print("You open the drawer.")
                time.sleep(3)
                print("It is empty.")
                time.sleep(3)
            elif response == "Two" or response == "two":
                print("You open the second drawer.")
                time.sleep(3)
                # Check if the player has already picked up the batteries.
                if self.batteries == True:
                    print("It is empty.")
                    time.sleep(3)
                else:
                    print("You find some batteries in the drawer.")
                    time.sleep(3)
                    print("This could power something.")
                    self.batteries = True
                    time.sleep(3)
            elif response == "Four" or response == "four":
                print("You open the fourth drawer.")
                time.sleep(3)
                # Check if the player has already picked up the big key.
                if self.big_key == True:
                    print("This drawer is empty")
                    time.sleep(3)
                else:
                    print("There is a big key here.")
                    time.sleep(3)
                    print("This could be used to open the front door maybe.")
                    self.big_key = True
                    time.sleep(3)
            elif response == "Explore" or response == "explore":
                pass
            else:
                print("Invalid input, try again.")
    


    def Desk(self):
        """
        Runs the code for when the player interacts with the desk.
        The player can read the note and pick up the token.
        """
        print("You look over at the desk and see a note.")
        # Checks if the player has already picked up the token or not.
        if self.token == False:
            print("You also see a small token.")
            time.sleep(3)
            print("It looks like it could be used in a washing machine.")
            time.sleep(3)
            print("You pick it up.")
            self.token = True
            time.sleep(3)
        print("You pick up the note and read it.")
        time.sleep(3)
        print("It reads:")
        time.sleep(3)
        print("'YOU did THIS to ME")
        print("You will regret everything...'")
        time.sleep(3)
        print("You put the note back down.")
        time.sleep(3)