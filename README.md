**Bulls and Cows** 

Also known as Mastermind, this is a game in which one attempts to guess a 4-digit code.  With every guess, one is told  how many digits they guessed correctly and in the right place, and how many digits they guessed correctly, but got in the wrong place.  

Example:  Let's assume the correct code is 1234.  If you guess 1256, you will get the following response:

> Number of digits in the right place: 2
> Number of digits guessed correctly but in the wrong place: 0

If you guess 1243, you will get:

> Number of digits in the right place: 2
> Number of digits guessed correctly but in the wrong place: 2

Most implementations of this game simply tell you that you got "2 bulls and 2 cows"; however, I wanted this game to be playable without having read the manual or having any knowledge about the game.

This game has now been ported to Python3.  I will be packaging it for the Arch User Repository very soon.  If you'd like to package it for other distros, go for it.  I also encourage you to try to port this game to any programming or scripting language that you want to learn better.  It's a fun little excercise in loops, basic boolean logic, and command line I/O, and perfect for a beginner who's tired of writing "Hello world" and making fizzbuzzes.  

**TODO**:
* Package for AUR


If anyone wants to fork this and play around with it, I welcome them.  
