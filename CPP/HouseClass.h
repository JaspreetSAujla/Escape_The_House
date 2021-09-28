#include<iostream>
#include "PlayerClass.h"
#include "ObjectClass.h"
using namespace std;

#ifndef HOUSECLASS_H
#define HOUSECLASS_H

class House {
    /*
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
    
    public:
        Player player;

        House();

        House(string RoomName);

        void move();
    
    private:
        Objects objects;
        string roomName;

        void livingRoom();

        void kitchen();

        void hallway();

        void bathroom();

        void basement();

        void bedroom();

        void attic();

        void door();
};

#endif