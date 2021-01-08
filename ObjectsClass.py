from PlayerClass import Player
import random
import time

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
            time.sleep(3)
            print("You need to turn on the power first.")
            time.sleep(3)
        else:
            print("You turn on the TV.")
            time.sleep(3)
            print("You see some static and the screen flashes.")
            time.sleep(3)
            print("You see the digits '247274' on the screen.")
            time.sleep(3)
            print("The TV turns off...")
            time.sleep(3)
    


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
        sounds = ["'You will never escape...'",
                  "'Are you trying to leave?'",
                  "'Do you know what happened here??'",
                  "'Can you discover my secret...'"]
        
        # Checks whether the player has picked up the batteries.
        if character.batteries == False:
            print("The radio is powered by batteries.")
            time.sleep(3)
            print("You need to find some batteries first.")
            time.sleep(3)
        else:
            print("You turn on the radio.")
            time.sleep(3)
            print("You hear a faint sound.")
            time.sleep(3)
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
            time.sleep(3)
            print("It looks like you need a token key to open it.")
            time.sleep(3)
        else:
            print("You have the token key to open the washing machine.")
            time.sleep(3)
            print("You open it and are hit by a strong smell.")
            time.sleep(3)
            print("You reach in and grab what seems to be a top.")
            time.sleep(3)
            print("The top is covered in a dark red liquid...")
            time.sleep(3)
            print("You put the top back inside.")
            time.sleep(3)
    


    def Painting(self):
        """
        Runs the code for when the player interacts with the painting.
        """
        print("You look at the painting.")
        time.sleep(3)
        print("It is of a woman who is sat on an armchair.")
        time.sleep(3)
        print("You get fixed into her eyes...")
        time.sleep(3)
        print("The woman suddenly jumps out at you and pushes you to the ground.")
        time.sleep(3)
        print("You stumble back and look at the painting again.")
        time.sleep(3)
        print("You see her sat in her armchair as if she had not moved.")
        time.sleep(3)
    


    def Mirror(self):
        """
        Runs the code for when the player interacts with the mirror.
        """
        print("You look into the mirror.")
        time.sleep(3)
        print("It is dark and gloomy and you can barely see yourself.")
        time.sleep(3)
        print("You blink and see a woman behind you.")
        time.sleep(3)
        print("She reaches out to grab you by the neck.")
        time.sleep(3)
        print("You blink again and she is gone...")
        time.sleep(3)
    


    def Window(self):
        """
        Runs the code for when the player interacts with the window.
        """
        print("You step towards the window and look outside.")
        time.sleep(3)
        print("You see a small garden surrounded by trees.")
        time.sleep(3)
        print("At the far end of the garden, you see a figure.")
        time.sleep(3)
        print("It looks like a woman and she seems somewhat familiar.")
        time.sleep(3)
        print("A flash of lightning erupts in the sky and she disappears...")
        time.sleep(3)
    


    def Chest(self, character):
        """
        Runs the code for when the player interacts with the chest.
        If the player has the small key, then the chest will open.
        """
        # Checks if the player has the small key.
        if character.small_key == False:
            print("It looks like the chest needs a key to open.")
            time.sleep(3)
        else:
            print("You use the small key to open the chest.")
            time.sleep(3)
            print("You find a note inside.")
            time.sleep(3)
            print("It contains the number '512121'")
            time.sleep(3)
            print("Who knows what this could be for.")
            time.sleep(3)