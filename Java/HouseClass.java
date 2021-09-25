package Java;

import java.util.Scanner;

class House {
    /**
    This class creates an object that contains all the rooms of the house.
    An instance of this class is therefore a house object.

    Parameters:
        RoomName = Takes the name of the room the character is in. 
                   This will be set to the living room by default.
    
    Methods:
        House = initialises the instance of the class.
                Takes a default argument of 'living'.
        
        move = Allows the player to navigate through the house.

        livingRoom = Runs the code for when the player enters the 
                     living room.

        kitchen = Runs the code for when the player enters the kitchen.

        hallway = Runs the code for when the player enters the upstairs 
                  hallway.

        bathroom = Runs the code for when the player enters the bathroom.

        basement = Runs the code for when the player enters the basement.

        bedroom = Runs the code for when the player enters the bedroom.

        attic = Runs the code for when the player eneters the attic.

        door = Runs the code for when the player tries to open the door.
    */
    private String roomName;
    private Objects objects;
    public Player player;
    private Scanner scn;



    House(String RoomName) {
        /**
        This method defines the initial variables when an object is 
        instantiated.

        Variables:
            this.roomName = Takes the name of the room the character is in.
                            This will be set to the living room by default.

            this.objects = Creates an instance of the object class.
                           This populates the rooms with non-essential objects.
            
            this.character = Defines the character object as a variable of 
                             the instance of this class.
                             Allows character methods to be used and 
                             variables to be changed.
            
            this.scn = The scanner.
        */
        this.roomName = RoomName;
        this.objects = new Objects();
        this.player = new Player();
        this.scn = new Scanner(System.in);
    }



    public void move() {
        /**
        This method allows the user to move around the house.
        The user can only move to rooms next to their current room.
        This is handled by using an 'if' statement.
        */
        if (this.roomName.equals("living")) {
            livingRoom();
        } else if (this.roomName.equals("door")) {
            door();
        } else if (this.roomName.equals("kitchen")) {
            kitchen();
        } else if (this.roomName.equals("hallway")) {
            hallway();
        } else if (this.roomName.equals("bathroom")) {
            bathroom();
        } else if (this.roomName.equals("bedroom")) {
            bedroom();
        } else if (this.roomName.equals("basement")) {
            basement();
        } else if (this.roomName.equals("attic")) {
            attic();
        }
    }



    private void livingRoom() {
        /**
        This method defines the actions taken within the living room.
        The player will have the option to interact with objects and 
        choose to move rooms.

        Variables:
            moveRooms = This variables allows the player to interact 
                        with the objects as many times
                        as they want before moving rooms.
                        Set to False by default.

            option = The option picked by the player is stored in this 
                     variable.
                     Set to None as default.

            validMove = Checks if the room entered for moving is valid 
                        or not.
                        Set to False as default.
        */
        boolean moveRooms = false;
        boolean validMove = false;
        String option;

        // Code to describe the room to the player.
        System.out.println("You are in the living room.");
        System.out.println("There is a TV here.");
        System.out.println("The stairs are on your right and the kitchen is at the back.");
        System.out.println("The front door is behind you.");

        // While loop to interact with objects.
        while (moveRooms == false) {
            System.out.println("What would you like to do?");
            System.out.println("Move rooms or watch tv?");
            System.out.println("(tv/move)");
            option = this.scn.nextLine();

            if (option.equals("tv")) {
                this.objects.tv(this.player);
            } else if (option.equals("move")) {
                moveRooms = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
        // Loops over till valid room is picked.
        while (validMove == false) {
            System.out.println("Which room would you like to move to?");
            System.out.println("The kitchen, upstairs hallway or try the front door.");
            System.out.println("(Kitchen/Hallway/Door)");
            this.roomName = this.scn.nextLine();

            if (this.roomName.equals("kitchen") || this.roomName.equals("hallway") || this.roomName.equals("door")) {
                validMove = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
    }



    private void kitchen() {
        /**
        This method defines the actions taken when the player enters 
        the kitchen.
        The player can interact with objects and move rooms.

        Variables:
            moveRooms = This variables allows the player to interact 
                        with the objects as many times
                        as they want before moving rooms.
                        Set to False by default.

            option = The option picked by the player is stored in this 
                     variable.
                     Set to None as default.

            validMove = Checks if the room entered for moving is valid 
                        or not.
                        Set to False as default.
        */
        boolean moveRooms = false;
        boolean validMove = false;
        String option;

        // Code to describe the room to the player.
        System.out.println("You are in the kitchen.");
        System.out.println("There is a radio on the table.");
        System.out.println("There are stairs leading down to the basement and the living room is next to you.");

        while (moveRooms == false) {
            System.out.println("What would you like to do?");
            System.out.println("Turn on the radio or move rooms?");
            System.out.println("(radio/move)");
            option = this.scn.nextLine();

            if (option.equals("radio")) {
                this.objects.radio(this.player);
            } else if (option.equals("move")) {
                moveRooms = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
        while (validMove == false) {
            System.out.println("Which room would you like to move to?");
            System.out.println("The basement or living room?");
            System.out.println("(Basement/Living)");
            this.roomName = this.scn.nextLine();
            if (this.roomName.equals("basement") || this.roomName.equals("living")) {
                validMove = true;
            } else {
                System.out.println("Invalid move, try again.");
            }
        }
    }



    private void hallway() {
        /**
        This method defines the actions taken when the player enters 
        the upstairs hallway.
        The player can interact with the painting or move rooms.

        Variables:
            moveRooms = This variables allows the player to interact 
                        with the objects as many times
                        as they want before moving rooms.
                        Set to False by default.

            option = The option picked by the player is stored in this 
                     variable.
                     Set to None as default.

            validMove = Checks if the room entered for moving is valid 
                        or not.
                        Set to False as default.
        */
        boolean moveRooms = false;
        boolean validMove = false;
        String option;

        // Code to describe the hallway to the player.
        System.out.println("You are in the upstairs hallway.");
        System.out.println("There is a painting on the wall.");
        System.out.println("There are doors leading to the bedroom, bathroom and attic.");
        System.out.println("There are also stairs leading down to the living room.");

        while (moveRooms == false) {
            System.out.println("What would you like to do?");
            System.out.println("Look at the painting or move rooms?");
            System.out.println("(painting/move)");
            option = this.scn.nextLine();

            if (option.equals("painting")) {
                this.objects.painting();
            } else if (option.equals("move")) {
                moveRooms = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
        while (validMove == false) {
            System.out.println("Which room would you like to move to?");
            System.out.println("The bedroom, bathroom, attic or living room?");
            System.out.println("(Bedroom/Bathroom/Attic/Living)");
            this.roomName = this.scn.nextLine();
            if (this.roomName.equals("bedroom") || this.roomName.equals("bathroom") || this.roomName.equals("attic") || this.roomName.equals("living")) {
                validMove = true;
            } else {
                System.out.println("Invalid move, try again.");
            }
        }
    }



    private void bathroom() {
        /**
        This method defines the actions the player can take when they 
        enter the bathroom.
        The player can pick up the power back or look at the mirror.

        Variables:
            option = The option picked by the player is stored in 
                     this variable.
                     Set to None as default.
            
            leaveBathroom = Stores whether the player wants to 
                            leave the bathroom or not.
        */
        String option;
        boolean leaveBathroom = false;

        // Code to describe the bathroom.
        System.out.println("You are in the bathroom.");
        System.out.println("There is a mirror on the wall.");
        System.out.println("There is also a bath with the shower curtain closed.");

        while (leaveBathroom == false) {
            System.out.println("What do you do?");
            System.out.println("Look in the mirror, look in the bath or go back to the hallway?");
            System.out.println("(mirror/bath/hallway)");
            option = this.scn.nextLine();

            if (option.equals("bath")) {
                this.player.bath();
            } else if (option.equals("mirror")) {
                this.objects.mirror();
            } else if (option.equals("hallway")) {
                leaveBathroom = true;
                this.roomName = "hallway";
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
    }



    private void basement() {
        /**
        This method defines the actions the player can take when 
        they enter the basement.
        The player can try to turn on the power or interact with 
        the washing machine.

        Variables:
            option = The option picked by the player is stored in 
                     this variable.
                     Set to None as default.
            
            leaveBasement = Stores whether the player wants to 
                            leave the basement or not.
        */
        String option;
        boolean leaveBasement = false;

        // Code to describe the basement.
        System.out.println("You walk down the stairs to the basement.");
        System.out.println("It is dark and there is one little light bulb glowing dimly.");
        System.out.println("There is a power generator in front of you.");
        System.out.println("There is also a washing machine in the corner.");

        while (leaveBasement == false) {
            System.out.println("What do you do?");
            System.out.println("Turn on the power, open the washing machine or go back to the kitchen?");
            System.out.println("(power/washing/kitchen)");
            option = this.scn.nextLine();

            if (option.equals("power")) {
                this.player.generator();
            } else if (option.equals("washing")) {
                this.objects.washingMachine(this.player);
            } else if (option.equals("kitchen")) {
                this.roomName = "kitchen";
                leaveBasement = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
    }



    private void bedroom() {
        /**
        This method defines the actions the player can take when 
        they enter the bedroom.
        They can interact with the safe, or look at the nightstand.

        Variables:
            option = The option picked by the player is stored in 
                     this variable.
                     Set to None as default.
            
            leaveBedroom = Stores whether the player wants to 
                           leave the bedroom or not.
        */
        String option;
        boolean leaveBedroom = false;

        // Code to describe the bedroom.
        System.out.println("You are in the bedroom.");
        System.out.println("You see a safe in the corner of the room as well as a nightstand next to the bed.");
        System.out.println("You also see a window but the blinds are closed.");

        while (leaveBedroom == false) {
            System.out.println("What do you want to do?");
            System.out.println("Look out of the window, look at the nightstand, open the safe or go back to the hallway?");
            System.out.println("(window/stand/safe/hallway");
            option = this.scn.nextLine();

            if (option.equals("window")) {
                this.objects.window();
            } else if (option.equals("stand")) {
                this.player.nightstand(this.scn);
            } else if (option.equals("safe")) {
                this.player.safe(this.scn);
            } else if (option.equals("hallway")) {
                this.roomName = "hallway";
                leaveBedroom = true;
            } else {
                System.out.println("Invalid response, try again.");
            }
        }
    }



    private void attic() {
        /**
        This method runs the code for when the player enters the attic.
        The player can interact with the desk or the chest.

        Variables:
            option = The option picked by the player is stored in this 
                     variable.
                     Set to None as default.
            
            leaveAttic = Stores whether the player wants to leave the 
                         attic or not.
        */
        String option;
        boolean leaveAttic = false;

        // Code to describe the attic.
        System.out.println("You are in the attic.");
        System.out.println("It is dark and humid.");
        System.out.println("You see a chest and a desk.");

        while (leaveAttic == false) {
            System.out.println("What do you do?");
            System.out.println("Look in the chest, examine the desk or return to the hallway?");
            System.out.println("(chest/desk/hallway)");
            option = this.scn.nextLine();

            if (option.equals("chest")) {
                this.objects.chest(this.player);
            } else if (option.equals("desk")) {
                this.player.desk();
            } else if (option.equals("hallway")) {
                this.roomName = "hallway";
                leaveAttic = true;
            } else {
                System.out.println("Invalid input, try again.");
            }
        }
    }



    private void door() {
        /**
        Runs the code for when the player tries to open the door.
        If the player has turned on the power
        and got the key and knows the alarm code,
        then they can escape.

        Variables:
            response = Stores the response of the player.
                       They can either guess the password or explore.
                       Set to None by default.
            
            codeGuess = Stores what the player thinks the code is.
                        Used to check if the player is correct.
                        Set to None by default.
            
            explore = Stores whether the player wants to continue 
                      exploring or not.
        */
        String response;
        String codeGuess;
        boolean explore = false;

        System.out.println("You try to open the door.");
        if (this.player.bigKey == true && this.player.power == true) {
            System.out.println("The power is on.");
            System.out.println("This has turned on the alarm system.");
            System.out.println("You must enter the password to escape.");

            while (explore == false) {
                System.out.println("What do you do?");
                System.out.println("Guess the password or carry on exploring?");
                System.out.println("(guess/explore)");
                response = this.scn.nextLine();

                if (response.equals("guess")) {
                    System.out.println("The alarm requires a 6-digit code.");
                    System.out.println("What is your guess?");
                    codeGuess = this.scn.nextLine();
                    if (codeGuess.equals("512121")) {
                        System.out.println("That is the correct code.");
                        System.out.println("You put the key in the door and unlock it.");
                        this.player.escaped = true;
                        break;
                    } else {
                        System.out.println("That is not the correct code.");
                    }
                } else if (response.equals("explore")) {
                    this.roomName = "living";
                    explore = true;
                } else {
                    System.out.println("Invalid input, try again.");
                }
            }
        } else if (this.player.bigKey == true && this.player.power == false) {
            System.out.println("You have the key to open the door.");
            System.out.println("However, the door is connected to the mains.");
            System.out.println("You need to turn on the power first.");
            this.roomName = "living";
        } else if (this.player.bigKey == false) {
            System.out.println("You need a key to open the door.");
            this.roomName = "living";
        }
    }
}