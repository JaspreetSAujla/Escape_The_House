package Java;

public class EscapeHouseGame {
    /**
    Class which initialises and runs the escaoe from the house game.
    
    Methods:
        EscapeHouseGame = Initialises the variables.
        
        runGame = Runs the game.
    */
    private House house;



    EscapeHouseGame() {
        /**
        Defines the initial variables of the game.
        
        Variables:
            this.house = Defines a house object.
        */
        this.house = new House("living");

        // Introduce the game.
        System.out.println("You wake up out of a slumber. \nYou appear to be on the floor.");
        System.out.println("Looking around, you find yourself in a dark living room.");
        System.out.println("You cannot remember the events leading up to this, but you know you must escape.");
        System.out.println("The house is old and creaky; the wind is blowing hard outside");
        System.out.println("The windows are all boarded up.");
    }



    public void runGame() {
        /**
        Runs the code for the game.
        Loops over until the player has escaped.
        */
        while (this.house.player.escaped == false) {
            this.house.move();
        }
        // Code for when the player escapes the house.
        System.out.println("You open the door and step outside.");
        System.out.println("You are hit with bright lights and sirens.");
        System.out.println("The police are outside waiting for you.");
        System.out.println("You are handcuffed and taken into custody.");
        System.out.println("You are told that you are under arrest for the ");
        System.out.println("murder of the woman who lived in the house.");
        System.out.println("You look down and see that your hands are covered in blood.");
        System.out.println("Maybe it was you all along...");
    }
}