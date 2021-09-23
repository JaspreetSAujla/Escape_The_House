from HouseClass import House
import time

class EscapeHouseGame:
    """
    Class which initialises and runs the escaoe from the house game.
    
    Methods:
        __init__ = Initialises the variables.
        
        run_game = Runs the game.
    """



    def __init__(self):
        """
        Defines the initial variables of the game.
        
        Variables:
            self.house = Defines a house object.
        """
        self.house = House(RoomName = "living")

        # Introduce the game.
        print("You wake up out of a slumber. \nYou appear to be on the floor.")
        time.sleep(1)
        print("Looking around, you find yourself in a dark living room.")
        time.sleep(1)
        print("You cannot remember the events leading up to this, but you know you must escape.")
        time.sleep(1)
        print("The house is old and creaky; the wind is blowing hard outside")
        time.sleep(1)
        print("The windows are all boarded up.")
        time.sleep(1)
    


    def run_game(self):
        """
        Runs the code for the game.
        Loops over until the player has escaped.
        """
        while self.house.character.escaped == False:
            self.house.move()
        
        # Code for when the player escapes the house.
        print("You open the door and step outside.")
        time.sleep(3)
        print("You are hit with bright lights and sirens.")
        time.sleep(3)
        print("The police are outside waiting for you.")
        time.sleep(3)
        print("You are handcuffed and taken into custody.")
        time.sleep(3)
        print("You are told that you are under arrest for the ")
        print("murder of the woman who lived in the house.")
        time.sleep(3)
        print("You look down and see that your hands are covered in blood.")
        time.sleep(3)
        print("Maybe it was you all along...")