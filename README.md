# VoidScript

---
###### VoidScript is a new space themed programming language built in python

---

## How to use:
* Clone the repo
* Create a .vs file in the same directory as `voidscript.py`
* Write your code into the .vs file
* Open your terminal and type `python voidscript.py <filename>.vs`
* Press enter and the code will run

## Features:
* New spaced theme syntax 
* Error messages
* New features like _Wormhole_

## Syntax:
* **LOG**: print stuff in the terminal. Examples: `LOG Hello World`, `LOG 1 2` (prints Hello World / 1 2 in the terminal)
* **VAR**: declare and modify variables. Examples: `VAR x = 0`, `VAR x + 1` (declares the variable x (name) with the value 0. Increases x by one). `VAR y = Hello` (string also possible)
    * LOG + VAR: `LOG {x}`, `LOG {x / 2}` (prints the value of x in the terminal / the value of x divided by two)
* **IF**: checks whether a condition is true or false. Examples: `IF x = 2 : LOG x is two ~ LOG x is something else` (if the variable x has the value 2 then (`:`) `x is two` will be printed. Else (`~`) `x is something else` will be printed.)
* **BLACKHOLE**: allows the user to input something. The input is then the value of a variable. Example: `VAR input = BLACKHOLE` (the user can now input everything. `input`'s value is the input)
* **WORMHOLE_TO**: jumps to the line. Example: `WORMHOLE_TO 12` (jumps to the line 12. Skips everthing else. Usefull for loops)
    * WORMHOLE_TO + IF: `IF distance = 100 : WORMHOLE_TO 17 ~ WORMHOLE_TO 15` (while distance is smaller than 100, the code will jump to line 15, distance will be increased. If 100 the code will jump to line 17 and continue)
* **WORMHOLE**: jumps x lines. Example: `WORMHOLE 2` (jumps two lines)

## Example:
![whole](https://cloud-7lptp4za5-hack-club-bot.vercel.app/0whole.png)

* Output:

![0](https://cloud-23ezl6601-hack-club-bot.vercel.app/00.png)

or

![1](https://cloud-lg87w57nm-hack-club-bot.vercel.app/01.png)

## Info:
* This project was done without any tutorial because I wanted to try it on my own.
* More features are planned (random, arrays)

## Credits:
* Code: Qwatrum

made with <3 by Qwatrum