package Java;

import java.util.Random;

class Objects {
    /**
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

    Objects() {}



    public void tv(Player player) {
        /**
        Runs the code for when the player interacts with the TV.
        If the power is on, a 6 digit code will display.
        If not, nothing will happen.

        Parameters:
            player = Allows the player object to be used in the function.
                     This is used to check if the power is on.
        */
        // Checks if the player has turned on the power or not.
        if (player.power == false) {
            System.out.println("The TV is connected to the mains.");
            System.out.println("You need to turn on the power first.");
        } else {
            System.out.println("You turn on the TV.");
            System.out.println("You see some static and the screen flashes.");
            System.out.println("You see the digits '247274' on the screen.");
            System.out.println("The TV turns off...");
        }
    }



    public void radio(Player player) {
        /**
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
            
            randomNumber = Generates a random number to be used 
                           to pick a sound randomly.
        */
        Random randomNumber = new Random();
        String[] sounds = {"'You will never escape...'",
                           "'Are you trying to leave?'",
                           "'Do you know what happened here??'",
                           "'Can you discover my secret...'"};

        // Checks whether the player has picked up the batteries.
        if (player.batteries == false) {
            System.out.println("The radio is powered by batteries.");
            System.out.println("You need to find some batteries first.");
        } else {
            System.out.println("You turn on the radio.");
            System.out.println("You hear a faint sound.");
            System.out.println(sounds[randomNumber.nextInt(sounds.length)]);
        }
    }



    public void washingMachine(Player player) {
        /**
        Runs the code for when the player interacts with the washing machine.
        If the player has the token, the washing machine will open.

        Parameters:
            player = Allows the player object to be used in the function.
                     Checks whether the player has the token or not.
        */
        // Use if statement to check if player has the token.
        if (player.token == false) {
            System.out.println("The washing machine will not open.");
            System.out.println("It looks like you need a token key to open it.");
        } else {
            System.out.println("You have the token key to open the washing machine.");
            System.out.println("You open it and are hit by a strong smell.");
            System.out.println("You reach in and grab what seems to be a top.");
            System.out.println("The top is covered in a dark red liquid...");
            System.out.println("You put the top back inside.");
        }
    }



    public void mirror() {
        /**
        Runs the code for when the player interacts with the mirror.
        */
        System.out.println("You look into the mirror.");
        System.out.println("It is dark and gloomy and you can barely see yourself.");
        System.out.println("You blink and see a woman behind you.");
        System.out.println("She reaches out to grab you by the neck.");
        System.out.println("You blink again and she is gone...");
    }



    public void painting() {
        /**
        Runs the code for when the player interacts with the painting.
        */
        System.out.println("You look at the painting.");
        System.out.println("It is of a woman who is sat on an armchair.");
        System.out.println("You get fixed into her eyes...");
        System.out.println("The woman suddenly jumps out at you and pushes you to the ground.");
        System.out.println("You stumble back and look at the painting again.");
        System.out.println("You see her sat in her armchair as if she had not moved.");
    }



    public void window() {
        /**
        Runs the code for when the player interacts with the window.
        */
        System.out.println("You step towards the window and look outside.");
        System.out.println("You see a small garden surrounded by trees.");
        System.out.println("At the far end of the garden, you see a figure.");
        System.out.println("It looks like a woman and she seems somewhat familiar.");
        System.out.println("A flash of lightning erupts in the sky and she disappears...");
    }



    public void chest(Player player) {
        /**
        Runs the code for when the player interacts with the chest.
        If the player has the small key, then the chest will open.

        Parameters:
            player = Passes in the character to check if the 
                     player has a small key or not.
        */
        // Checks if the player has the small key.
        if (player.smallKey == false) {
            System.out.println("It looks like the chest needs a key to open.");
        } else {
            System.out.println("You use the small key to open the chest.");
            System.out.println("You find a note inside.");
            System.out.println("It contains the number '512121'");
            System.out.println("Who knows what this could be for.");
        }
    }
}