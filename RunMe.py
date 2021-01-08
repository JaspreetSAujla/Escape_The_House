from RoomClass import Rooms
import time

if __name__ == "__main__":
    # Define the variables.
    house = Rooms("living")          # Creates a house object.

    # Introduce the game.
    print("You wake up out of a slumber. \nYou appear to be on the floor.")
    time.sleep(3)
    print("Looking around, you find yourself in a dark living room.")
    time.sleep(3)
    print("You cannot remember the events leading up to this, but you know you must escape.")
    time.sleep(3)
    print("The house is old and creaky; the wind is blowing hard outside")
    time.sleep(3)
    print("The windows are all boarded up.")
    time.sleep(3)
    # Calls the living room function to start the game.
    house.LivingRoom()

    # Loops over until player has escaped.
    while house.character.escaped == False:
        house.Move()
    
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