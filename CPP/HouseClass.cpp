#include<iostream>
#include "PlayerClass.h"
#include "ObjectClass.h"
#include "HouseClass.h"
using namespace std;

House::House() {}

House::House(string RoomName) {
    /*
    This method defines the initial variables when an object is 
    instantiated.

    Variables:
        this->roomName = Takes the name of the room the character is in.
                         This will be set to the living room by default.

        this->objects = Creates an instance of the object class.
                        This populates the rooms with non-essential objects.
            
        this->character = Defines the character object as a variable of 
                          the instance of this class.
                          Allows character methods to be used and 
                          variables to be changed.
    */
    this->roomName = RoomName;
    this->objects = Objects();
    this->player = Player();
}



void House::move() {
    /*
    This method allows the user to move around the house.
    The user can only move to rooms next to their current room.
    This is handled by using an 'if' statement.
    */
    if (this->roomName == "living") {
        livingRoom();
    } else if (this->roomName == "door") {
        door();
    } else if (this->roomName == "kitchen") {
        kitchen();
    } else if (this->roomName == "hallway") {
        hallway();
    } else if (this->roomName == "bathroom") {
        bathroom();
    } else if (this->roomName == "bedroom") {
        bedroom();
    } else if (this->roomName == "basement") {
        basement();
    } else if (this->roomName == "attic") {
        attic();
    }
}



void House::livingRoom() {
    /*
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
    bool moveRooms = false;
    bool validMove = false;
    string option;

    // Code to describe the room to the player.
    cout << "You are in the living room. \n";
    cout << "There is a TV here. \n";
    cout << "The stairs are on your right and the kitchen is at the back. \n";
    cout << "The front door is behind you. \n";

    // While loop to interact with objects.
    while (moveRooms == false) {
        cout << "What would you like to do? \n";
        cout << "Move rooms or watch tv? \n";
        cout << "(tv/move) \n";
        cin >> option;

        if (option == "tv") {
            this->objects.tv(this->player);
        } else if (option == "move") {
            moveRooms = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
    // Loops over till valid room is picked.
    while (validMove == false) {
        cout << "Which room would you like to move to? \n";
        cout << "The kitchen, upstairs hallway or try the front door. \n";
        cout << "(Kitchen/Hallway/Door) \n";
        cin >> this->roomName;

        if (this->roomName == "kitchen" || this->roomName == "hallway" || this->roomName == "door") {
            validMove = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
}



void House::kitchen() {
    /*
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
    bool moveRooms = false;
    bool validMove = false;
    string option;

    // Code to describe the room to the player.
    cout << "You are in the kitchen. \n";
    cout << "There is a radio on the table. \n";
    cout << "There are stairs leading down to the basement and the living room is next to you. \n";

    while (moveRooms == false) {
        cout << "What would you like to do? \n";
        cout << "Turn on the radio or move rooms? \n";
        cout << "(radio/move) \n";
        cin >> option;

        if (option == "radio") {
            this->objects.radio(this->player);
        } else if (option == "move") {
            moveRooms = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
    while (validMove == false) {
        cout << "Which room would you like to move to? \n";
        cout << "The basement or living room? \n";
        cout << "(Basement/Living) \n";
        cin >> this->roomName;
        if (this->roomName == "basement" || this->roomName == "living") {
            validMove = true;
        } else {
            cout << "Invalid move, try again. \n";
        }
    }
}



void House::hallway() {
    /*
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
    bool moveRooms = false;
    bool validMove = false;
    string option;

    // Code to describe the hallway to the player.
    cout << "You are in the upstairs hallway. \n";
    cout << "There is a painting on the wall. \n";
    cout << "There are doors leading to the bedroom, bathroom and attic. \n";
    cout << "There are also stairs leading down to the living room. \n";

    while (moveRooms == false) {
        cout << "What would you like to do? \n";
        cout << "Look at the painting or move rooms? \n";
        cout << "(painting/move) \n";
        cin >> option;

        if (option == "painting") {
            this->objects.painting();
        } else if (option == "move") {
            moveRooms = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
    while (validMove == false) {
        cout << "Which room would you like to move to? \n";
        cout << "The bedroom, bathroom, attic or living room? \n";
        cout << "(Bedroom/Bathroom/Attic/Living) \n";
        cin >> this->roomName;
        if (this->roomName == "bedroom" || this->roomName == "bathroom" || this->roomName == "attic" || this->roomName == "living") {
            validMove = true;
        } else {
            cout << "Invalid move, try again. \n";
        }
    }
}



void House::bathroom() {
    /*
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
    string option;
    bool leaveBathroom = false;

    // Code to describe the bathroom.
    cout << "You are in the bathroom. \n";
    cout << "There is a mirror on the wall. \n";
    cout << "There is also a bath with the shower curtain closed. \n";

    while (leaveBathroom == false) {
        cout << "What do you do? \n";
        cout << "Look in the mirror, look in the bath or go back to the hallway? \n";
        cout << "(mirror/bath/hallway) \n";
        cin >> option;

        if (option == "bath") {
            this->player.bath();
        } else if (option == "mirror") {
            this->objects.mirror();
        } else if (option == "hallway") {
            leaveBathroom = true;
            this->roomName = "hallway";
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
}



void House::basement() {
    /*
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
    string option;
    bool leaveBasement = false;

    // Code to describe the basement.
    cout << "You walk down the stairs to the basement. \n";
    cout << "It is dark and there is one little light bulb glowing dimly. \n";
    cout << "There is a power generator in front of you. \n";
    cout << "There is also a washing machine in the corner. \n";

    while (leaveBasement == false) {
        cout << "What do you do? \n";
        cout << "Turn on the power, open the washing machine or go back to the kitchen? \n";
        cout << "(power/washing/kitchen) \n";
        cin >> option;

        if (option == "power") {
            this->player.generator();
        } else if (option == "washing") {
            this->objects.washingMachine(this->player);
        } else if (option == "kitchen") {
            this->roomName = "kitchen";
            leaveBasement = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
}



void House::bedroom() {
    /*
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
    string option;
    bool leaveBedroom = false;

    // Code to describe the bedroom.
    cout << "You are in the bedroom. \n";
    cout << "You see a safe in the corner of the room as well as a nightstand next to the bed. \n";
    cout << "You also see a window but the blinds are closed. \n";

    while (leaveBedroom == false) {
        cout << "What do you want to do? \n";
        cout << "Look out of the window, look at the nightstand, open the safe or go back to the hallway? \n";
        cout << "(window/stand/safe/hallway) \n";
        cin >> option;

        if (option == "window") {
            this->objects.window();
        } else if (option == "stand") {
            this->player.nightstand();
        } else if (option == "safe") {
            this->player.safe();
        } else if (option == "hallway") {
            this->roomName = "hallway";
            leaveBedroom = true;
        } else {
            cout << "Invalid response, try again. \n";
        }
    }
}



void House::attic() {
    /*
    This method runs the code for when the player enters the attic.
    The player can interact with the desk or the chest.

    Variables:
        option = The option picked by the player is stored in this 
                 variable.
                 Set to None as default.
        
        leaveAttic = Stores whether the player wants to leave the 
                     attic or not.
    */
    string option;
    bool leaveAttic = false;

    // Code to describe the attic.
    cout << "You are in the attic. \n";
    cout << "It is dark and humid. \n";
    cout << "You see a chest and a desk. \n";

    while (leaveAttic == false) {
        cout << "What do you do? \n";
        cout << "Look in the chest, examine the desk or return to the hallway? \n";
        cout << "(chest/desk/hallway) \n";
        cin >> option;

        if (option == "chest") {
            this->objects.chest(this->player);
        } else if (option == "desk") {
            this->player.desk();
        } else if (option == "hallway") {
            this->roomName = "hallway";
            leaveAttic = true;
        } else {
            cout << "Invalid input, try again. \n";
        }
    }
}



void House::door() {
    /*
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
    string response;
    string codeGuess;
    bool explore = false;

    cout << "You try to open the door. \n";
    if (this->player.bigKey == true && this->player.power == true) {
        cout << "The power is on. \n";
        cout << "This has turned on the alarm system. \n";
        cout << "You must enter the password to escape. \n";

        while (explore == false) {
            cout << "What do you do? \n";
            cout << "Guess the password or carry on exploring? \n";
            cout << "(guess/explore) \n";
            cin >> response;

            if (response == "guess") {
                cout << "The alarm requires a 6-digit code. \n";
                cout << "What is your guess? \n";
                cin >> codeGuess;
                if (codeGuess == "512121") {
                    cout << "That is the correct code. \n";
                    cout << "You put the key in the door and unlock it. \n";
                    this->player.escaped = true;
                    break;
                } else {
                    cout << "That is not the correct code. \n";
                }
            } else if (response == "explore") {
                this->roomName = "living";
                explore = true;
            } else {
                cout << "Invalid input, try again. \n";
            }
        }
    } else if (this->player.bigKey == true && this->player.power == false) {
        cout << "You have the key to open the door. \n";
        cout << "However, the door is connected to the mains. \n";
        cout << "You need to turn on the power first. \n";
        this->roomName = "living";
    } else if (this->player.bigKey == false) {
        cout << "You need a key to open the door. \n";
        this->roomName = "living";
    }
}