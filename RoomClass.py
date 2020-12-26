from ObjectsClass import Objects

class Rooms:
    """
    This class creates an object that contains all the rooms of the house.
    An instance of this class is therefore a house object.

    Parameters:
        RoomName = Takes the name of the room the character is in. 
                   This will be set to the living room by default.
    
    Methods:
        __init__ = initialises the instance of the class.
                   Takes a default argument of 'living'.

        Move = Allows the player to navigate through the house.

        LivingRoom = Runs the code for when the player enters the living room.

        Kitchen = Runs the code for when the player enters the kitchen.
    """

    def __init__(self, RoomName="living"):
        """
        This method defines the initial variables when an object is instantiated.

        Variables:
            self.room_name = Takes the name of the room the character is in. 
                             This will be set to the living room by default.

            self.objects = Creates an instance of the object class.
                           This populates the rooms with non-essential objects.
        """
        self.room_name = RoomName
        self.objects = Objects()
    


    def Move(self):
        """
        This method allows the user to move around the house.
        The user can only move to rooms next to their current room.
        This is handled by using an 'if' statement.
        """
        # This block is used to move into the living room.
        if self.room_name == "living" or self.room_name == "Living":
            self.LivingRoom()
        # This block is used to move into the kitchen.
        elif self.room_name == "Kitchen" or self.room_name == "kitchen":
            self.Kitchen()
    


    def LivingRoom(self):
        """
        This method defines the actions taken within the living room.
        The player will have the option to interact with objects and choose to move rooms.

        Variables:
            move_rooms = This variables allows the player to interact with the objects as many times
                         as they want before moving rooms.
                         Set to False by default.

            option = The option picked by the player is stored in this variable.
                     Set to None as default.

            valid_move = Checks if the room entered for moving is valid or not.
                         Set to False as default.
        """
        move_rooms = False
        option = None
        valid_move = False

        # Code to describe the room to the player.
        print("You are in the living room.")
        print("There is a TV here.")
        print("The stairs are on your right and the kitchen is at the back.")
        print("The front door is behind you.")

        # While loop allows player to interact with objects as many times as they like.
        while move_rooms == False:
            print("What would you like to do?")
            print("Turn on the TV, or move rooms?")
            option = input("(TV/Move) \n")
            # This block allows the player to interact with the TV.
            if option == "TV" or option == "Tv" or option == "tv":
                pass
            # Allows player to move rooms.
            elif option == "Move" or option == "move":
                move_rooms = True
            # Prompts the user to try again if input is invalid.
            else:
                print("Invalid input, try again.")
        
        # Loops over if room is not valid.
        while valid_move == False:
            print("Which room would you like to move to?")
            print("(Kitchen/Upstaurs/Door)")
            self.room_name = input()
            # If statement checks the name is valid to escape the while loop.
            if self.room_name == "Kitchen" or self.room_name == "kitchen" or self.room_name == "Upstairs" or self.room_name == "upstairs" or self.room_name == "Door" or self.room_name == "door":
                valid_move = True
            else:
                print("Not a valid room, try again.")
    


    def Kitchen(self):
        """
        This method defines the actions taken when the player enters the kitchen.
        The player can interact with objects and move rooms.

        Variables:
            move_rooms = This variables allows the player to interact with the objects as many times
                         as they want before moving rooms.
                         Set to False by default.

            option = The option picked by the player is stored in this variable.
                     Set to None as default.

            valid_move = Checks if the room entered for moving is valid or not.
                         Set to False as default.
        """
        move_rooms = False
        option = None
        valid_move = False

        # Code to describe the room to the player.
        print("You are in the kitchen.")
        print("There is a radio on the table.")
        print("There are stairs leading down to the basement and the living room is next to you.")

        # While loop allows player to interact with objects as many times as they like.
        while move_rooms == False:
            print("What would you like to do?")
            print("Turn on the radio or move rooms?")
            option = input("(Radio/Move) \n")
            # This block allows player to interact with the radio.
            if option == "Radio" or option == "radio":
                pass
            # Allows player to move rooms.
            elif option == "Move" or option == "move":
                move_rooms = True
            # Prompts player to put a valid input.
            else:
                print("Not a valid input, try again.")
        
        # Loops over if room is not valid.
        while valid_move == False:
            print("Which room would you like to move to>")
            print("The basement or living room?")
            print("(Basement/Living)")
            self.room_name = input()
            # If statement checks the name is valid to escape the while loop.
            if self.room_name == "Basement" or self.room_name == "basement" or self.room_name == "Living" or self.room_name == "living":
                valid_move = True
            else:
                print("Not a valid room, try again.")