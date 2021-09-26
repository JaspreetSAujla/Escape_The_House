#include<iostream>
#include "PlayerClass.h"
using namespace std;

Player::Player() {
    /*
    This method defines the initial variables when the person object 
    is created.

    Variables:
        this->escaped = This will track whether the player is allowed 
                       to escape or not.
                       All the essential tasks need to be completed 
                       to escape.
                       Set to False by default.

        this->power = This will check whether the player has turned 
                     on the power.
                     Power needs to be turned on for value to become 
                     True.
                     Set to False by default.
            
        this->batteries = Checks whether the player has picked up the 
                         batteries.
                         Batteries can be used in the radio.
                         Set to False by default.
            
        this->powerPack = Checks whether the player has picked up the 
                         power pack.
                         Power pack used to turn power back on.
                         Set to False by default.
            
        this->token = Checks whether the player has picked up the token 
                     to open the
                     washing machine.
                     Set to False by default.

        this->smallKey = Checks whether the player has picked up the 
                        small key 
                        to open the chest in the attic.
                        Set to False by defualt.
            
        this->bigKey = Checks whether the player has picked up the big 
                      key
                      to open the front door and escape.
                      Set to False by default.
    */
    this->batteries = false;
    this->bigKey = false;
    this->escaped = false;
    this->power = false;
    this->powerPack = false;
    this->smallKey = false;
    this->token = false;
}



void Player::bath() {
    /*
    Runs the code for when the player interacts with the bath.
    If the player does not have the power pack already,
    then they can pick it up.
    Otherwise the bath will be empty.
    */
    // Use if statement to check if player has picked up the 
    // power pack already.
    if (this->powerPack == false) {
        cout << "There seems to be something in the bath. \n";
        cout << "You find a power pack; this could be useful later. \n";
        this->powerPack = true;
    } else {
        cout << "There is nothing in the bath. \n";
    }
}



void Player::generator() {
    /*
    Runs the code for when the player interacts with the generator.
    If the player has the power pack, they will be able to turn on 
    the power.
    If not, the power will remain off.
    If the power is already on, it will stay on.
    */
    // If statment to check if the player has the power pack.
    if (this->powerPack == false) {
        cout << "The power will not turn on. \n";
        cout << "It seems like it is missing a power pack. \n";
    } else if (this->power == true) {
        cout << "The power is already on. \n";
    } else {
        cout << "You have a power pack. \n";
        cout << "You place the power pack into the generator. \n";
        cout << "You hear some noise and the power turns on. \n";
        this->power = true;
    }
}



void Player::safe() {
    /*
    Runs the code for when the player interacts with the safe.
    The player has to input the correct password to open the safe.
    The safe contains the small key to open the chest in the attic.

    Variables:
        codeGuess = Contains the players guess for the code.
                    Set to None by default.

        tryAgain = Checks if the player wants to keep guessing or not.
                   Set to True by default.
            
        response = Checks what the response is for the player wanting 
                   to try again.
                   Set to None by default.
    */
    string codeGuess;
    bool tryAgain = true;
    string response;

    cout << "You look at the safe. \n";
    cout << "You see that it needs a 6-digit code to unlock. \n";

    // While loop to see if the player wants to keep guessing.
    while (tryAgain == true) {
        cout << "What is your guess? \n";
        cin >> codeGuess;
        // Check if the code guess is correct.
        if (codeGuess == "247274") {
            cout << "That is the correct code. \n";
            cout << "The safe opens... \n";
            // Checks if the player already has the small key.
            if (this->smallKey == true) {
                cout << "The safe is empty. \n";
            } else {
                cout << "You look inside and find a small key. \n";
                cout << "This looks like it could be used for the front door. \n";
                cout << "Or something else maybe... \n";
                this->smallKey = true;
            }
            tryAgain = false;
        } else {
            cout << "That is the incorrect code. \n";
            cout << "Would you like to try again? \n(yes/no) \n";
            cin >> response;
            if (response == "no") {
                tryAgain = false;
            }
        }
    }
}



void Player::nightstand() {
    /*
    Runs the code for when the player interats with the nightstand.
    The player can read the note or open the drawers.

    Variables:
        response = Allows the player to interact with the nightstand
                   as many times as they like.
                   Set to None by default.
            
        explore = Stores whether the player wants to continue 
                  exploring or not.
    */
    string response;
    bool explore = false;

    cout << "You look at the nightstand and see a note on top of it. \n";
    cout << "The nightstand also has 4 drawers on it. \n";

    // While loop to allow player to interact with nightstand as long 
    // as they want.
    while (explore == false) {
        cout << "What do you do? \n";
        cout << "Read the note, open 1 of the 4 drawers or continue exploring? \n";
        cout << "(Note/One/Two/Three/Four/Explore) \n";
        cin >> response;

        if (response == "note") {
            cout << "You pick up the note and read it. \n";
            cout << "It reads: \n";
            cout << "'She is in the house \n";
            cout << "Leave while you can \n";
            cout << "I did not want to do this to her...' \n";
            cout << "You put the note down. \n";
        } else if (response == "one" || response == "three") {
            cout << "You open the drawer \n";
            cout << "It is empty. \n";
        } else if (response == "two") {
            cout << "You open the second drawer. \n";
            // Checks to see if the player already has the batteries.
            if (this->batteries == true) {
                cout << "it is empty. \n";
            } else {
                cout << "You find some batteries in the drawer. \n";
                cout << "This could power something. \n";
                this->batteries = true;
            }
        } else if (response == "four") {
            cout << "You open the fourth drawer. \n";
            // Check to see if player already has the big key.
            if (this->bigKey == true) {
                cout << "The drawer is empty. \n";
            } else {
                cout << "You find a big key. \n";
                cout << "This could be used to open the front door maybe. \n";
                this->bigKey = true;
            }
        } else if (response == "explore") {
            explore = true;
        } else {
            cout << "Invalid response, try again. \n";
        }
    }
}



void Player::desk() {
    /*
    Runs the code for when the player interacts with the desk.
    The player can read the note and pick up the token.
    */
    cout << "You look over at the desk and see a note. \n";
    // Checks if the player has already picked up the token or not.
    if (this->token == false) {
        cout << "You also see a small token. \n";
        cout << "It looks like it could be used in a washing machine. \n";
        cout << "You pick it up. \n";
        this->token = true;
    }
    cout << "You pick up the note and read it. \n";
    cout << "It reads: \n";
    cout << "'YOU did THIS to ME \n";
    cout << "You will regret everything...' \n";
    cout << "You put the note back down. \n";
}