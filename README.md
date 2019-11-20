# Roboto-Royale

Roboto Royale

Project Description:
	A battle royale top-down side scrolling game with 2.5d graphics. There will be a randomly generated map each time the game is launched and items will be scattered throughout the map. The goal is to be the last man standing as players face against bots or maybe other players by picking up weapons and other items such as healthups scattered in the map and dodgerolling or shooting to kill the enemies.

Competitive Analysis:
	This is taken with the inspiration of the critically acclaimed Steam game, Super Animal Battle Royale. It is similar as both have 2.5d graphics and battle royale mode with similar mechanics such as dodge rolling. There is also similarity in that the bullets and fov will be blocked by obstacles. I will also include bots which is similar as well, however my bots will only follow simple paths. The difference is the theme which mine will be around robots and have lesser map complexity, because it will be randomly generated as opposed to Super Animal Battle Royale.
	Another similar project could be tanks such as the behavior in WII Play which the bullets follow similar projections as well as contain visually similar elements as it is a top down design. Also, the behavior of bots will be similar as well. 

Structural Plan:
	I will be using pygamgame.py in order to make it easier to write the main game mode of the game. The main game will be in the main file. I will have a superclass called gameObject with the basics for initializing and updating objects in the game. The objects specifically I will incorporate will be the items, obstacles like trees and wood, bullets, the player, and the enemy. The main file will be in charge of initializing all these objects, updating the map and generating the random layout, while I will use the specific object class to incorporate specific behaviors. Under update, I will incorporate most of the movements and change in order to make the transition as seamless as possible. I also have an image folder that contains all the sprites that will be used for the term project.

Algorithmic Plan:
	The most difficult part of the project would be the algorithm for the bots and area of view mechanism. 
	Bot Algorithm
	The bot itself will be a subclass of the player class	
I will split the bots’ algorithm into 3 parts: Moving, Shooting, Dodging
For Moving, the bot will move in the forward direction, with probabilities to stop, turn, and go backwards every few seconds which will be in the update method
For Shooting, I will create an arc from the bot sprite that acts like its field of view. It will check for players in the update section. Once, it “sees” a player, it will move the arc to track the player until the player disappears by hiding behind an obstacle and fire bullets in a random angle within that arc. The harder the difficulty, the smaller the arc. Bullet rate will also depend on the difficulty.
For Dodging, if the bullet comes at them, then it will have a probability of moving right, left or dodge-rolling to move out of the way

Area of View
This will be an arc similar to the bots view, except it will be around where the mouse direction is. Then, if the view will be drawn brighter in the arc as opposed to the other parts of the map until it hits an obstacle. If there is an enemy, if the line between the enemy and the player is not blocked by an obstacle, then the enemy will be visible. If it is, then the enemy will be invisible. I will do this by getting the location of the enemies and player and then getting the line between them and checking if there is an obstacle. Enemies will have a isVisible and if False, then they will not be drawn.

Timeline Plan:
	I plan to have the map side scrolling and fog of war viewing done by Thursday. By Saturday, I plan to complete a basic bot algorithm as well as finish the random map generation. By Sunday, I intend to finish the construction of houses. Monday and Tuesday will encompass the other game modes, health bar, and timer until game starts as well as fix bugs.

Version Control:
	I will be using github to commit and push any major changes as a way to have access to previous versions and be able to track my changes.

Module List:
	pygame

