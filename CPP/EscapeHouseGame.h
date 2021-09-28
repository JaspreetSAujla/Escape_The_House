#include<iostream>
#include "HouseClass.h"
using namespace std;

#ifndef ESCAPEHOUSEGAME_H
#define ESCAPEHOUSEGAME_H

class EscapeHouseGame {
    /*
    Class which initialises and runs the escaoe from the house game.
    
    Methods:
        EscapeHouseGame = Initialises the variables.
        
        runGame = Runs the game.
    */
    
    public:
        EscapeHouseGame();

        void runGame();

    private:
        House house;
};

#endif