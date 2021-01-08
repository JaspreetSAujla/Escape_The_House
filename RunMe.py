from RoomClass import Rooms

if __name__ == "__main__":
    # Define the variables.
    house = Rooms("living")          # Creates a house object.

    # Introduce the game.
    print("You wake up out of a slumber. \nYou apprear to be on the floor.")
    print("Looking around, you find yourself in a dark living room.")
    print("You cannot remember the events leading up to this, but you know you must escape.")
    print("The house is old and creaky; the wind is blowing hard outside")
    print("The windows are all boarded up.")
    # Calls the living room function to start the game.
    house.LivingRoom()

    # Loops over until player has escaped.
    while house.character.escaped == False:
        house.Move()
    
    # Code for when the player escapes the house.
    print("You open the door and step outside.")
    print("You are hit with bright lights and sirens.")
    print("The police are outside waiting for you.")
    print("You are handcuffed and taken into custody.")
    print("You are told that you are under arrest for the ")
    print("murder of the woman who lived in the house.")
    print("You look down and see that your hands are covered in blood.")
    print("Maybe it was you all along...")