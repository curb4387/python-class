## Your Tasks

The `play` method in the `Player` class of the craps game plays an entire game without interaction with the user. Revise the `Player` class (in the file **craps.py**) so that its user can make individual rolls of the dice and view the results after each roll. The `Player` class no longer accumulates a list of rolls, but saves the string representation of
each roll after it is made.

Add new methods `rollDice`, `getNumberOfRolls`, `isWinner`, and `isLoser` to the `Player` class. The last three methods allow the user to obtain the number of rolls and to determine whether there is a winner or a loser. The last two methods are associated with new Boolean instance variables (`winner` and `loser` respectively). Two other instance variables track the number of rolls and the string representation of the most recent roll (`rollsCount` and `roll`). Another instance variable (`atStartup`) tracks whether or not the first roll has occurred.

At instantiation, the `roll`, `rollsCount`, `atStartup`, `winner`, and `loser` variables are set to their appropriate initial values. All game logic is now in the `rollDice` method. This method rolls the dice once, updates the state of the `Player` object, and returns a tuple of the values of the dice for that roll. Include in the module the `playOneGame` and `playManyGames` functions, suitably updated for the new interface to the `Player` class. (LO: 10.1, 10.2)

## Instructions
