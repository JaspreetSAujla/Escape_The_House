from ObjectsClass import Objects
from PlayerClass import Player

class Rooms:
    """
    This class creates an object that contains all the rooms of the house.
    An instance of this class is therefore a house object.

    Parameters:
        Character = Takes the character object defined in the main file.
                    This will allow character methods and variables to be changed accordingly.

        RoomName = Takes the name of the room the character is in. 
                   This will be set to the living room by default.
    
    Methods:
        __init__ = initialises the instance of the class.
                   Takes a default argument of 'living'.

        Move = Allows the player to navigate through the house.

        LivingRoom = Runs the code for when the player enters the living room.

        Kitchen = Runs the code for when the player enters the kitchen.

        Hallway = Runs the code for when the player enters the upstairs hallway.

        Bathroom = Runs the code for when the player enters the bathroom.

        Basement = Runs the code for when the player enters the basement.

        Bedroom = Runs the code for when the player enters the bedroom.

        Attic = Runs the code for when the player eneters the attic.
    """

    def __init__(self, Character, RoomName="living"):
        """
        This method defines the initial variables when an object is instantiated.

        Variables:
            self.room_name = Takes the name of the room the character is in. 
                             This will be set to the living room by default.

            self.objects = Creates an instance of the object class.
                           This populates the rooms with non-essential objects.
            
            self.character = Defines the character object as a variable of the instance of this class.
                             Allows character methods to be used and variables to be changed.
        """
        self.room_name = RoomName
        self.objects = Objects()
        self.character = Character
    


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
        # This block is used to move into the hallway.
        elif self.room_name == "Hallway" or self.room_name == "hallway":
            self.Hallway()
        # This block is used to move into the bathroom.
        elif self.room_name == "Bathroom" or self.room_name == "bathroom":
            self.Bathroom()
        # This block is used to move into the basement.
        elif self.room_name == "Basement" or self.room_name == "basement":
            self.Basement()
        # This block is used to move into the bedroom.
        elif self.room_name == "Bedroom" or self.room_name == "bedroom":
            self.Bedroom()
        # This block is used to move into the attic.
        elif self.room_name == "Attic" or "attic":
            self.Attic()
    


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
                # Checks if the player has turned on the power or not.
                if self.character.power == False:
                    print("The Tv is connected to the mains.")
                    print("You need to turn on the power first.")
                else:
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
            print("The kitchen, upstairs hallway or try the front door.")
            print("(Kitchen/Hallway/Door)")
            self.room_name = input()
            # If statement checks the name is valid to escape the while loop.
            if self.room_name == "Kitchen" or self.room_name == "kitchen" or self.room_name == "Hallway" or self.room_name == "hallway" or self.room_name == "Door" or self.room_name == "door":
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
                # Checks whether the player has picked up the batteries.
                if self.character.batteries == False:
                    print("The radio is powered by batteries.")
                    print("You need to find some batteries first.")
                else:
                    pass
            # Allows player to move rooms.
            elif option == "Move" or option == "move":
                move_rooms = True
            # Prompts player to put a valid input.
            else:
                print("Not a valid input, try again.")
        
        # Loops over if room is not valid.
        while valid_move == False:
            print("Which room would you like to move to?")
            print("The basement or living room?")
            print("(Basement/Living)")
            self.room_name = input()
            # If statement checks the name is valid to escape the while loop.
            if self.room_name == "Basement" or self.room_name == "basement" or self.room_name == "Living" or self.room_name == "living":
                valid_move = True
            else:
                print("Not a valid room, try again.")
    


    def Hallway(self):
        """
        This method defines the actions taken when the player enters the upstairs hallway.
        The player can interact with the painting or move rooms.

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

        # Code to describe the hallway to the player.
        print("You are in the upstairs hallway.")
        print("There is a painting on the wall.")
        print("There are doors leading to the bedroom, bathroom and attic.")
        print("There are also stairs leading down to the living room.")

        # While loop allows player to interact with objects as many times as they want.
        while move_rooms == False:
            print("What would you like to do?")
            print("Look at the painting or move rooms?")
            option = input("(Painting/Move) \n")
            # This block allows the player to interact with the painting.
            if option == "Painting" or option == "painting":
                pass
            # Allows player to move rooms.
            elif option == "Move" or option == "move":
                move_rooms = True
            # Prompts player to put valid input.
            else:
                print("Not a valid input, try again.")
        
        # Loops over if room is not valid.
        while valid_move == False:
            print("Which room would you like to move to?")
            print("The bedroom, bathroom, attic or living room?")
            print("(Bedroom/Bathroom/Attic/Living)")
            self.room_name = input()
            # If statement checks if the name is valid to escape while loop.
            if self.room_name == "Bedroom" or self.room_name == "bedroom" or self.room_name == "Bathroom" or self.room_name == "bathroom" or self.room_name == "Attic" or self.room_name == "attic" or self.room_name == "Living" or self.room_name == "living":
                valid_move = True
            else:
                print("Not a valid room, try again.")
    


    def Bathroom(self):
        """
        This method defines the actions the player can take when they enter the bathroom.
        The player can pick up the power back or look at the mirror.

        Variables:
            option = The option picked by the player is stored in this variable.
                     Set to None as default.
        """
        option = None

        # Code to describe the bathroom.
        print("You are in the bathroom.")
        print("There is a mirror on the wall.")
        print("There is also a bath with the shower curtain closed.")

        # While loop allows player to stay in bathroom as long as they like.
        while self.room_name != "Hallway" or self.room_name != "hallway":
            print("What do you do?")
            print("Look in the mirror, look in the bath or go back to the hallway?")
            option = input("(Mirror/Bath/Hallway) \n")
            # Use if statement to check for valid input and execute code.
            if option == "Mirror" or option == "mirror":
                pass
            elif option == "Bath" or option == "bath":
                # Use if statement to check if player has picked up the power pack already.
                if self.character.power_pack == False:
                    print("There seems to be something in the bath.")
                    print("You find a power pack; this could be useful later.")
                    self.character.power_pack = True
                    print(self.character.power_pack)
                else:
                    print("There is nothing in the bath.")
            elif option == "Hallway" or option == "hallway":
                # Escapes while loop.
                break
            else:
                print("Not a valid input, try again.")
        self.room_name = "hallway"
    


    def Basement(self):
        """
        This method defines the actions the player can take when they enter the basement.
        The player can try to turn on the power or interact with the washing machine.

        Variables:
            option = The option picked by the player is stored in this variable.
                     Set to None as default.
        """
        option = None

        # Code to describe the basement.
        print("You walk down the stairs to the basement.")
        print("It is dark and there is one little light bulb glowing dimly.")
        print("There is a power generator in front of you.")
        print("There is also a washing machine in the corner.")

        # While loop allows player to stay in basement as long as they like.
        while option != "Kitchen" or option != "kitchen":
            print("What do you do?")
            print("Turn on the power, open the washing machine or go back to the kitchen?")
            option = input("(Washing/Power/Kitchen) \n")
            # Use if statement to check for valid input.
            if option == "Washing" or option == "washing":
                # Use if statement to check if player has the token.
                if self.character.token == False:
                    print("The washing machine will not open.")
                    print("It looks like you need a token key to open it.")
                else:
                    print("You have the token key to open the washing machine.")
                    pass
            elif option == "Power" or option == "power":
                # If statment to check if the player has the power pack.
                if self.character.power_pack == False:
                    print("The power will not turn on.")
                    print("It seems like it is missing a power pack.")
                else:
                    print("You have a power pack.")
                    pass
            elif option == "Kitchen" or option == "kitchen":
                # Escapes the while loop.
                break
            else:
                print("Invalid input, try again.")
        self.room_name = "kitchen"
    


    def Bedroom(self):
        """
        This method defines the actions the player can take when they enter the bedroom.
        They can interact with the safe, or look at the nightstand.

        Variables:
            option = The option picked by the player is stored in this variable.
                     Set to None as default.
        """
        option = None

        # Code to describe the bedroom.
        print("You are in the bedroom.")
        print("You see a safe in the corner of the room as well as a nightstand next to the bed.")
        print("You also see a window but the blinds are closed.")

        # While loop allows player to stay in the bedroom as long as they like.
        while self.room_name != "Hallway" or self.room_name != "hallway":
            print("What do you do?")
            print("Look out of the window, look at the nightstand, open the safe or go back to the hallway?")
            option = input("(Window/Safe/Stand/Hallway) \n")
            # If statement checks for valid input.
            if option == "Window" or option == "window":
                pass
            elif option == "Safe" or option == "safe":
                pass
            elif option == "Stand" or option == "stand":
                pass
            elif option == "Hallway" or option == "hallway":
                # Escapes the while loop.
                break
            else:
                print("Not a valid input, try again.")
        self.room_name = "hallway"
    


    def Attic(self):
        """
        This method runs the code for when the player enters the attic.
        The player can interact with the desk or the chest.

        Variables:
            option = The option picked by the player is stored in this variable.
                     Set to None as default.
        """
        option = None

        # Code to describe the attic.
        print("You are in the attic.")
        print("It is dark and humid.")
        print("You see a chest and a desk.")

        # While loop allows player to stay in the attic for as long as they want.
        while self.room_name != "Hallway" or self.room_name != "hallway":
            print("What do you do?")
            print("Look in the chest, examine the desk or return to the hallway?")
            option = input("(Chest/Desk/Hallway) \n")
            # If statement checks for valid input.
            if option == "Chest" or option == "chest":
                # Checks if the player has the small key.
                if self.character.small_key == False:
                    print("It looks like the chest needs a key to open.")
                else:
                    pass
            elif option == "Desk" or option == "desk":
                pass
            elif option == "Hallway" or option == "hallway":
                # Escapes the while loop.
                break
            else:
                print("Not a valid room name, try again.")
        self.room_name = "hallway"