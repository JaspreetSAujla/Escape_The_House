from PlayerClass import Player
import random

class Objects:
    """
    This class defines the objects in the game that do not contribute to the player escaping.
    These objects are for purpose of telling the story.
    Each method will be a different object.

    Methods:
        __init__ = Dummy method to ensure code works as no variables need to be set.

        TV = Runs the code for when the player interacts with the TV.

        Radio = Runs the code for when the player interacts with the radio.

        WashingMachine = Runs the code for when the player interacts with the washing machine.

        Painting = Runs the code for when the player interacts with the painting.

        Mirror = Runs the code for when the player interacts with the mirror.

        Window = Runs the code for when the player interacts with the window.

        Chest = Runs the code for when the player interacts with the chest.
    """

    def __init__(self):
        """
        Dummy method to ensure the code works.
        """
        pass



    def TV(self, character):
        """
        Runs the code for when the player interacts with the TV.
        If the power is on, a 6 digit code will display.
        If not, nothing will happen.

        Parameters:
            characters = Allows the player object to be used in the function.
                         This is used to check if the power is on.
        """
        # Checks if the player has turned on the power or not.
        if character.power == False:
            print("The TV is connected to the mains.")
            print("You need to turn on the power first.")
        else:
            print("You turn on the TV.")
            print("You see some static and the screen flashes.")
            print("You see the digits '247274' on the screen.")
            print("The TV turns off...")
    


    def Radio(self, character):
        """
        Runs the code for when the player interacts with the radio.
        If the player has batteries, they can listen to the radio.
        Random sounds will be played each time.

        Parameters:
            character = Allows player object to be used in the function.
                        Checks if the player has batteries so the radio can be used.
        
        Variables:
            sounds = List of sounds that are played when the player interacts with the radio.
        """
        sounds = ["You will never escape...",
                  "Are you trying to leave?",
                  "Do you know what happened here??",
                  "Can you discover my secret..."]
        
        # Checks whether the player has picked up the batteries.
        if character.batteries == False:
            print("The radio is powered by batteries.")
            print("You need to find some batteries first.")
        else:
            print("You turn on the radio.")
            print("You hear a faint sound.")
            print(random.choice(sounds))
    


    def WashingMachine(self, character):
        """
        Runs the code for when the player interacts with the washing machine.
        If the player has the token, the washing machine will open.

        Parameters:
            character = Allows the player object to be used in the function.
                        Checks whether the player has the token or not.
        """
        # Use if statement to check if player has the token.
        if character.token == False:
            print("The washing machine will not open.")
            print("It looks like you need a token key to open it.")
        else:
            print("You have the token key to open the washing machine.")
            print("You open it and are hit by a strong smell.")
            print("You reach in and grab what seems to be a top.")
            print("The top is covered in a dark red liquid...")
            print("You put the top back inside.")
    


    def Painting(self):
        """
        Runs the code for when the player interacts with the painting.
        """
        print("You look at the painting.")
        print("It is of a woman who is sat on an armchair.")
        print("You get fixed into her eyes...")
        print("The woman suddenly jumps out at you and pushes you to the ground.")
        print("You stumble back and look at the painting again.")
        print("You see her sat in her armchair as if she had not moved.")
    


    def Mirror(self):
        """
        Runs the code for when the player interacts with the mirror.
        """
        print("You look into the mirror.")
        print("It is dark and gloomy and you can barely see yourself.")
        print("You blink and see a woman behind you.")
        print("She reaches out to grab you by the neck.")
        print("You blink again and she is gone...")
    


    def Window(self):
        """
        Runs the code for when the player interacts with the window.
        """
        print("You step towards the window and look outside.")
        print("You see a small garden surrounded by trees.")
        print("At the far end of the garden, you see a figure.")
        print("It looks like a woman and she seems somewhat familiar.")
        print("A flash of lightning erupts in the sky and she disappears...")
    


    def Chest(self, character):
        """
        Runs the code for when the player interacts with the chest.
        If the player has the small key, then the chest will open.
        """
        # Checks if the player has the small key.
        if character.small_key == False:
            print("It looks like the chest needs a key to open.")
        else:
            print("You use the small key to open the chest.")
            print("You find a note inside.")
            print("It contains the number '512121'")
            print("Who knows what this could be for.")