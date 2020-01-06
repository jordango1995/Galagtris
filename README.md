# Galagtris
DESCRIPTION:

A work in progress of a game that is a combination of Galaga and Tetris. The player controls a single cell white ship and tries to fire shots at the enemy ship above. The enemy ship cycles through the different shapes of the classic Tetris pieces that everybody has come to know and love. 

This project is not nearly complete and is more of a foundation that I will be continually working on. Future improvements include:
Organizing the main script into more subdirectories
Back/Center cell indicators
Powerups
Advanced difficulty settings (if you want to manually increase difficulty, for now it can be done by decreasing the 'delay' in the "Galagtris.py" file)
Enhanced enemy ship fire/movement randomization (and possibly some added intelligence)
Player ship customization
A new game mode that involves the falling block feature of Tetris
Possible mouse movement incorporation


The controls are: 

Left/Right keys to move player ship
Spacebar to fire
'p' to pause
'esc' to exit game
Right Shift to restart



GAME RULES:

Each enemy ship starts off as a classic Tetris shape. When you hit a cell of this original shape, you can hit either the Left, Right, Back, or Center cell of the ship (there exist a couple exceptions to this rule, such as the purely horizontal enemy ship). 

If you hit the Left or Right wing of the enemy ship, your score increases by 100 points and the enemy ship loses that cell and no longer has a defined Center cell (but it still has a Back cell). 

If you hit the Center cell of the enemy ship, it destroys the whole ship immediately and increases your score by 1,000 points.

If you hit the Back cell of the enemy ship, it heals the enemy ship and causes it to fire off three blasts as opposed to its usual attack pattern of a single blast. I.e. you don't want to hit the Back cell.

Lastly, if you have slowly worn away at the enemy ship and avoided hitting its Back cell, it will be wittled down to its Last cell. This means that hitting this cell will not heal the enemy ship. Instead, it will destroy it and increase the player's score by 500 points.

In the future, Center cells will be indicated with a slightly lighter color than the rest of the cells, and Back cells will be represented as slightly darker.




AN EXAMPLE: 

The enemy ship may look like this (L=Left cell, R=Right cell, B=Back cell, C=Center cell):


[L][B][R]     
   [C]
   
   
If you hit the left wing, the enemy ship will change to this:
 
 
   [B][R] 
   [L]
 
 
Note that the Center cell is no longer available. The next Tetris shape will have a new Center cell.


To play, download both files into a single directory and run the module "Galagtris.py" to launch the GUI and start the game. 
