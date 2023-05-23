# KLAX-Game
Implement the KLAX Game by store some Alphabets in the dictionary. When the Alphabets start flowing down, the user will click the following Alphabets letter and Select the alphabets and make the meaningful words from these alphabets. When the meaningful word will be generated then the user will get 10 points.

KLAX is a puzzle video game released in arcades in 1990 by Atari Games while Namco distributed the game in Japanese markets. It was designed by Dave Akers and Mark Stephen Pierce. The object is to catch colored blocks tumbling down a machine and arrange them in colored rows and patterns to make them disappear. In KLAX, players control a paddle that can move horizontally at the bottom of the screen. Colored tiles called "klaxons" drop from a conveyor belt at the top of the screen, and the player's objective is to catch and arrange these tiles in specific patterns or combinations. The patterns can include horizontal rows, diagonal lines, or stacks of the same color.
 
KLAX became popular due to its addictive gameplay, challenging levels, and simple yet engaging mechanics. It received positive reviews from players and critics alike and was ported to various gaming platforms, including the Sega Genesis, Nintendo Entertainment System (NES), and Commodore 64, among others. The player can hold up to five tiles at a time and drop them onto the playing field when desired. If the player successfully creates a pattern, the tiles are removed, and the player earns points. As the game progresses, the speed of the conveyor belt increases, adding to the challenge.

The Work Flow of the generated game is given below:
•	The program generates a random letter from the alphabet dictionary using the generate_random_letter() function.
•	The letter is displayed on the screen, and the user is prompted to enter a word or press 'Enter' to skip.
•	The program checks if the entered word contains the randomly generated letter.
•	If the letter is used in the word, it checks if the word is valid (present in the alphabet dictionary). If it is valid, the user earns 10 points; otherwise, no points are awarded.
•	The score is updated and displayed on the screen.
•	The process continues indefinitely, allowing the user to play as long as they want.

