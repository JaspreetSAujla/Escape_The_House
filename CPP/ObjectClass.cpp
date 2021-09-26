#include<iostream>
#include<vector>
#include "PlayerClass.h"
#include "ObjectClass.h"
#include "RandomNumber.h"
using namespace std;

Objects::Objects() {}



void Objects::tv(Player player) {
    /*
    Runs the code for when the player interacts with the TV.
    If the power is on, a 6 digit code will display.
    If not, nothing will happen.

    Parameters:
        player = Allows the player object to be used in the function.
                 This is used to check if the power is on.
    */
    // Checks if the player has turned on the power or not.
    if (player.power == false) {
        cout << "The TV is connected to the mains. \n";
        cout << "You need to turn on the power first. \n";
    } else {
        cout << "You turn on the TV. \n";
        cout << "You see some static and the screen flashes. \n";
        cout << "You see the digits '247274' on the screen. \n";
        cout << "The TV turns off... \n";
    }
}



void Objects::radio(Player player) {
    /*
    Runs the code for when the player interacts with the radio.
    If the player has batteries, they can listen to the radio.
    Random sounds will be played each time.

    Parameters:
        player = Allows player object to be used in the function.
                 Checks if the player has batteries so the radio 
                 can be used.
        
    Variables:
        sounds = List of sounds that are played when the player 
                 interacts with the radio.
    */
    vector<string> sounds = {"'You will never escape...'",
                             "'Are you trying to leave?'",
                             "'Do you know what happened here??'",
                             "'Can you discover my secret...'"};

    // Checks whether the player has picked up the batteries.
    if (player.batteries == false) {
        cout << "The radio is powered by batteries. \n";
        cout << "You need to find some batteries first. \n";
    } else {
        cout << "You turn on the radio. \n";
        cout << "You hear a faint sound. \n";
        cout << sounds[randomNumberGenerator(0, sounds.size())];
    }
}



void Objects::washingMachine(Player player) {
    /*
    Runs the code for when the player interacts with the washing machine.
    If the player has the token, the washing machine will open.

    Parameters:
        player = Allows the player object to be used in the function.
                 Checks whether the player has the token or not.
    */
    // Use if statement to check if player has the token.
    if (player.token == false) {
        cout << "The washing machine will not open. \n";
        cout << "It looks like you need a token key to open it. \n";
    } else {
        cout << "You have the token key to open the washing machine. \n";
        cout << "You open it and are hit by a strong smell. \n";
        cout << "You reach in and grab what seems to be a top. \n";
        cout << "The top is covered in a dark red liquid... \n";
        cout << "You put the top back inside. \n";
    }
}



void Objects::mirror() {
    /*
    Runs the code for when the player interacts with the mirror.
    */
    cout << "You look into the mirror. \n";
    cout << "It is dark and gloomy and you can barely see yourself. \n";
    cout << "You blink and see a woman behind you. \n";
    cout << "She reaches out to grab you by the neck. \n";
    cout << "You blink again and she is gone... \n";
}



void Objects::painting() {
    /*
    Runs the code for when the player interacts with the painting.
    */
    cout << "You look at the painting. \n";
    cout << "It is of a woman who is sat on an armchair. \n";
    cout << "You get fixed into her eyes... \n";
    cout << "The woman suddenly jumps out at you and pushes you to the ground. \n";
    cout << "You stumble back and look at the painting again. \n";
    cout << "You see her sat in her armchair as if she had not moved. \n";
}



void Objects::window() {
    /*
    Runs the code for when the player interacts with the window.
    */
    cout << "You step towards the window and look outside. \n";
    cout << "You see a small garden surrounded by trees. \n";
    cout << "At the far end of the garden, you see a figure. \n";
    cout << "It looks like a woman and she seems somewhat familiar. \n";
    cout << "A flash of lightning erupts in the sky and she disappears... \n";
}



void Objects::chest(Player player) {
    /*
    Runs the code for when the player interacts with the chest.
    If the player has the small key, then the chest will open.

    Parameters:
        player = Passes in the character to check if the 
                 player has a small key or not.
    */
    // Checks if the player has the small key.
    if (player.smallKey == false) {
        cout << "It looks like the chest needs a key to open. \n";
    } else {
        cout << "You use the small key to open the chest. \n";
        cout << "You find a note inside. \n";
        cout << "It contains the number '512121' \n";
        cout << "Who knows what this could be for. \n";
    }
}