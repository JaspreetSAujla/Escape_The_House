

class Player:
    """
    This class will define the player object.
    It will store the essential objects the player needs to escape.
    It will have methods to interact with the essential objects.

    Methods:
        __init__ = Sets the initial variables when the person object is created.
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
        """
        self.escaped = False
        self.power = False
        self.batteries = False