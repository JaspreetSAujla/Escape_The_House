package Java;

import java.util.Scanner;

class Player {
    /**
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
    public boolean escaped;
    public boolean power;
    public boolean batteries;
    public boolean powerPack;
    public boolean token;
    public boolean smallKey;
    public boolean bigKey;



    Player() {
        /**
        This method defines the initial variables when the person object 
        is created.

        Variables:
            this.escaped = This will track whether the player is allowed 
                           to escape or not.
                           All the essential tasks need to be completed 
                           to escape.
                           Set to False by default.

            this.power = This will check whether the player has turned 
                         on the power.
                         Power needs to be turned on for value to become 
                         True.
                         Set to False by default.
            
            this.batteries = Checks whether the player has picked up the 
                             batteries.
                             Batteries can be used in the radio.
                             Set to False by default.
            
            this.powerPack = Checks whether the player has picked up the 
                             power pack.
                             Power pack used to turn power back on.
                             Set to False by default.
            
            this.token = Checks whether the player has picked up the token 
                         to open the
                         washing machine.
                         Set to False by default.

            this.smallKey = Checks whether the player has picked up the 
                            small key 
                            to open the chest in the attic.
                            Set to False by defualt.
            
            this.bigKey = Checks whether the player has picked up the big 
                          key
                          to open the front door and escape.
                          Set to False by default.
        */
        this.batteries = false;
        this.bigKey = false;
        this.escaped = false;
        this.power = false;
        this.powerPack = false;
        this.smallKey = false;
        this.token = false;
    }



    public void bath() {
        /**
        Runs the code for when the player interacts with the bath.
        If the player does not have the power pack already,
        then they can pick it up.
        Otherwise the bath will be empty.
        */
        // Use if statement to check if player has picked up the 
        // power pack already.
        if (this.powerPack == false) {
            System.out.println("There seems to be something in the bath.");
            System.out.println("You find a power pack; this could be useful later.");
            this.powerPack = true;
        } else {
            System.out.println("There is nothing in the bath.");
        }
    }



    public void generator() {
        /**
        Runs the code for when the player interacts with the generator.
        If the player has the power pack, they will be able to turn on 
        the power.
        If not, the power will remain off.
        If the power is already on, it will stay on.
        */
        // If statment to check if the player has the power pack.
        if (this.powerPack == false) {
            System.out.println("The power will not turn on.");
            System.out.println("It seems like it is missing a power pack.");
        } else if (this.power == true) {
            System.out.println("The power is already on.");
        } else {
            System.out.println("You have a power pack");
            System.out.println("You place the power pack into the generator.");
            System.out.println("You hear some noise and the power turns on.");
            this.power = true;
        }
    }



    public void safe(Scanner scn) {
        /**
        Runs the code for when the player interacts with the safe.
        The player has to input the correct password to open the safe.
        The safe contains the small key to open the chest in the attic.

        Parameters:
            scn = Passes in the scanner.

        Variables:
            codeGuess = Contains the players guess for the code.
                        Set to None by default.

            tryAgain = Checks if the player wants to keep guessing or not.
                       Set to True by default.
            
            response = Checks what the response is for the player wanting 
                       to try again.
                       Set to None by default.
        */
        String codeGuess;
        boolean tryAgain = true;
        String response;

        System.out.println("You look at the safe");
        System.out.println("You see that it needs a 6-digit code to unlock.");

        // While loop to see if the player wants to keep guessing.
        while (tryAgain == true) {
            System.out.println("What is your guess?");
            codeGuess = scn.nextLine();
            // Check if the code guess is correct.
            if (codeGuess.equals("247274")) {
                System.out.println("That is the correct code.");
                System.out.println("The safe opens...");
                // Checks if the player already has the small key.
                if (this.smallKey == true) {
                    System.out.println("The safe is empty.");
                } else {
                    System.out.println("You look inside and find a small key.");
                    System.out.println("This looks like it could be used for the front door.");
                    System.out.println("Or something else maybe...");
                    this.smallKey = true;
                }
                tryAgain = false;
            } else {
                System.out.println("That is the incorrect code.");
                System.out.println("Would you like to try again? \r\n(yes/no)");
                response = scn.nextLine();
                if (response.equals("no")) {
                    tryAgain = false;
                }
            }
        }
    }



    public void nightstand(Scanner scn) {
        /**
        Runs the code for when the player interats with the nightstand.
        The player can read the note or open the drawers.

        Parameters:
            scn = Passes in the scanner.

        Variables:
            response = Allows the player to interact with the nightstand
                       as many times as they like.
                       Set to None by default.
            
            explore = Stores whether the player wants to continue 
                      exploring or not.
        */
        String response;
        boolean explore = false;

        System.out.println("You look at the nightstand and see a note on top of it.");
        System.out.println("The nightstand also has 4 drawers on it.");

        // While loop to allow player to interact with nightstand as long 
        // as they want.
        while (explore == false) {
            System.out.println("What do you do?");
            System.out.println("Read the note, open 1 of the 4 drawers or continue exploring?");
            System.out.println("(Note/One/Two/Three/Four/Explore)");
            response = scn.nextLine();

            if (response.equals("note")) {
                System.out.println("You pick up the note and read it.");
                System.out.println("It reads:");
                System.out.println("'She is in the house");
                System.out.println("Leave while you can");
                System.out.println("I did not want to do this to her...'");
                System.out.println("You put the note down.");
            } else if (response.equals("one") || response.equals("three")) {
                System.out.println("You open the drawer");
                System.out.println("It is empty.");
            } else if (response.equals("two")) {
                System.out.println("You open the second drawer.");
                // Checks to see if the player already has the batteries.
                if (this.batteries == true) {
                    System.out.println("it is empty");
                } else {
                    System.out.println("You find some batteries in the drawer.");
                    System.out.println("This could power something.");
                    this.batteries = true;
                }
            } else if (response.equals("four")) {
                System.out.println("You open the fourth drawer.");
                // Check to see if player already has the big key.
                if (this.bigKey == true) {
                    System.out.println("The drawer is empty.");
                } else {
                    System.out.println("You find a big key.");
                    System.out.println("This could be used to open the front door maybe.");
                    this.bigKey = true;
                }
            } else if (response.equals("explore")) {
                explore = true;
            } else {
                System.out.println("Invalid response, try again.");
            }
        }
    }



    public void desk() {
        /**
        Runs the code for when the player interacts with the desk.
        The player can read the note and pick up the token.
        */
        System.out.println("You look over at the desk and see a note.");
        // Checks if the player has already picked up the token or not.
        if (this.token == false) {
            System.out.println("You also see a small token.");
            System.out.println("It looks like it could be used in a washing machine.");
            System.out.println("You pick it up.");
            this.token = true;
        }
        System.out.println("You pick up the note and read it.");
        System.out.println("It reads:");
        System.out.println("'YOU did THIS to ME");
        System.out.println("You will regret everything...'");
        System.out.println("You put the note back down.");
    }
}