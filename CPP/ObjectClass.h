#include<iostream>
#include "PlayerClass.h"
using namespace std;

#ifndef OBJECTCLASS_H
#define OBJECTCLASS_H

class Objects {
    /*
    This class defines the objects in the game that do not contribute 
    to the player escaping.
    These objects are for purpose of telling the story.
    Each method will be a different object.

    Methods:
        Objects = Dummy method to ensure code works as no variables 
                  need to be set.

        tv = Runs the code for when the player interacts with the TV.

        radio = Runs the code for when the player interacts with the radio.

        washingMachine = Runs the code for when the player interacts 
                         with the washing machine.

        painting = Runs the code for when the player interacts with the 
                   painting.

        mirror = Runs the code for when the player interacts with the mirror.

        window = Runs the code for when the player interacts with the window.

        chest = Runs the code for when the player interacts with the chest.
    */
    
    public:
        Objects();

        void tv(Player player);

        void radio(Player player);

        void washingMachine(Player player);

        void mirror();

        void painting();

        void window();

        void chest(Player player);
};

#endif