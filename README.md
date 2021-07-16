# Escape_The_House
You find yourself in a locked house. Explore what the house has to offer and try and find your way out...

# RunMe.py:
    To play the game, run this file.
    Runs the initial code to introduce the game.
    Calls the other files to allow for exploration of the house.

# RoomClass.py:
    This class creates an object that contains all the rooms of the house.
    An instance of this class is therefore a house object.

    Parameters:
        RoomName = Takes the name of the room the character is in. 
                   This will be set to the living room by default.
    
    Methods:
        __init__ = initialises the instance of the class.
                   Takes a default argument of 'living'.

        move = Allows the player to navigate through the house.

        living_room = Runs the code for when the player enters the living room.

        kitchen = Runs the code for when the player enters the kitchen.

        hallway = Runs the code for when the player enters the upstairs hallway.

        bathroom = Runs the code for when the player enters the bathroom.

        basement = Runs the code for when the player enters the basement.

        bedroom = Runs the code for when the player enters the bedroom.

        attic = Runs the code for when the player eneters the attic.

        door = Runs the code for when the player tries to open the door.

# ObjectsClass.py:
    This class defines the objects in the game that do not contribute to the player escaping.
    These objects are for purpose of telling the story.
    Each method will be a different object.

    Methods:
        __init__ = Dummy method to ensure code works as no variables need to be set.

        tv = Runs the code for when the player interacts with the TV.

        radio = Runs the code for when the player interacts with the radio.

        washing_machine = Runs the code for when the player interacts with the washing machine.

        painting = Runs the code for when the player interacts with the painting.

        mirror = Runs the code for when the player interacts with the mirror.

        window = Runs the code for when the player interacts with the window.

        chest = Runs the code for when the player interacts with the chest.

# PlayerClass.py:
    This class will define the player object.
    It will store the essential objects the player needs to escape.
    It will have methods to interact with the essential objects.

    Methods:
        __init__ = Sets the initial variables when the person object is created.

        bath = Runs the method for when the player interacts with the bath.

        generator = Runs the code for when the player interacts with the generator.

        safe = Runs the code for when the player interacts with the safe.

        nightstand = Runs the code for when the player interacts with the nightstand.

        desk = Runs the code for when the player interacts with the desk.