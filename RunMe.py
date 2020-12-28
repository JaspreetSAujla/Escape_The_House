from RoomClass import Rooms
from PlayerClass import Player

if __name__ == "__main__":
    # Define the variables.
    character = Player()                        # Creates a player object.
    house = Rooms(character, "living")          # Creates a house object.

    # Introduce the game.
    print("You wake up out of a slumber. \nYou apprear to be on the floor.")
    print("Looking around, you find yourself in a dark living room.")
    print("You cannot remember the events leading to this, but you know you must escape.")
    print("The house is old and creaky; the wind is blowing hard outside")
    print("The windows are all boarded up.")
    # Calls the living room function to start the game.
    house.LivingRoom()

    # Loops over until player has escaped.
    while character.escaped == False:
        house.Move()
