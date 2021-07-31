# Rock-Paper-Scissors-2021

## Jetbrains Academy Project | Level :  Medium

### About
![Advanced Rock Paper Scissor Game](https://umop.com/images/rps15.jpg "Advanced Rock Paper Scissor Game With 15 Options")
It's an advanced Rock-Paper-Scissors game.

Game options are : rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire

The game rules are in the following link:
https://umop.com/rps15.htm

##### How to play this game: 
1. At first, the game will ask the user their name.
2. Then it will ask the user to enter the options they want to use in the game (The comma has to be used to separate the options).
3. If the input is an empty line, the game will run using the default options (rock, paper, scissors).
4. User can see their score by typing '!rating'.
5. For each draw, the user will get 50 points. The user will be awarded 100 points for each win. The score will remain unchanged if the user loses.
6. If the input corresponds to anything else, 'Invalid input' will be displayed. 
7. The game will keep on running until the user types '!exit'. 


### Example Outputs:

##### Example 1: 
```
Enter your name: > Tim
Hello, Tim
> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Okay, let's start
> rock
Sorry, but the computer chose air
> !rating
Your rating: 0
> rock
Well done. The computer chose sponge and failed
> !rating
Your rating: 100
> !exit
Bye!
```
##### Example 2: 
```
Enter your name: > Tim
Hello, Tim
> 
Okay, let's start
> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but the computer chose rock
> !exit
Bye!
```

