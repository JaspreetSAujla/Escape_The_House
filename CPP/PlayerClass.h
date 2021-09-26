#include<iostream>
using namespace std;

#ifndef PLAYERCLASS_H
#define PLAYERCLASS_H

class Player {
    /*
    This class will define the player object.
    It will store the essential objects the player needs to escape.
    It will have methods to interact with the essential objects.

    Methods:
        Player = Sets the initial variables when the person object is created.

        bath = Runs the method for when the player interacts with the bath.

        generator = Runs the code for when the player interacts with the generator.

        safe = Runs the code for when the player interacts with the safe.

        nightstand = Runs the code for when the player interacts with the nightstand.

        desk = Runs the code for when the player interacts with the desk.
    */
    
    public:
        bool escaped;
        bool power;
        bool batteries;
        bool powerPack;
        bool token;
        bool smallKey;
        bool bigKey;

        Player();

        void bath();

        void generator();

        void safe();

        void nightstand();

        void desk();
};

#endif