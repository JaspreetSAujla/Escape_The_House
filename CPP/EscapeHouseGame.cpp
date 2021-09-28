#include<iostream>
#include "HouseClass.h"
#include "EscapeHouseGame.h"
using namespace std;

EscapeHouseGame::EscapeHouseGame() {
    /*
    Defines the initial variables of the game.
        
    Variables:
        this->house = Defines a house object.
    */
    this->house = House("living");

    // Introduce the game.
    cout << "You wake up out of a slumber. \nYou appear to be on the floor. \n";
    cout << "Looking around, you find yourself in a dark living room. \n";
    cout << "You cannot remember the events leading up to this, but you know you must escape. \n";
    cout << "The house is old and creaky; the wind is blowing hard outside \n";
    cout << "The windows are all boarded up. \n";
}



void EscapeHouseGame::runGame() {
    /*
    Runs the code for the game.
    Loops over until the player has escaped.
    */
    while (this->house.player.escaped == false) {
        this->house.move();
    }
    // Code for when the player escapes the house.
    cout << "You open the door and step outside. \n";
    cout << "You are hit with bright lights and sirens. \n";
    cout << "The police are outside waiting for you. \n";
    cout << "You are handcuffed and taken into custody. \n";
    cout << "You are told that you are under arrest for the  \n";
    cout << "murder of the woman who lived in the house. \n";
    cout << "You look down and see that your hands are covered in blood. \n";
    cout << "Maybe it was you all along... \n";
}