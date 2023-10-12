# MorseCodeRaspPI-Python
Turn both touch input from a sensor and keyboard input from a user and turn it into morse code via a buzzer on your Raspberry Pi.

# Materials List:
- Raspberry Pi-
  -![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/d8ae4ce2-6f92-474e-8a72-6a09a1a513c9)

	- This will be the mini computer you connect your circuits to and run your python scripts on.
- A T-Cobbler Plus - GPIO Breakout
	- ![[Pasted image 20231012092148.png|100x100]]
	- I use this to make the connection of circuits to my Pi via the breadboard easier. You don't absolutely need this but it may be hard to follow my tutorial without it.
- Breadboard -
	- ![[Pasted image 20231011110844.png|100x100]]
	- This will be the means you use to connect the circuits to your Raspberry Pi. This is a non-permanent way to make circuits for your Pi.
- 1x Touch Module -
	- ![[Pasted image 20231011110302.png|100x100]]
	- This is the touch sensor we will be using to receive touch input from our user. 
- 6x Female to Male Jumper Cables-
	- ![[Pasted image 20231011111047.png|100x100]]
	- These 6 cables are going to be used to connect your touch sensor and your buzzer to your Pi via the breadboard.
- 1x Active Buzzer (white sticker)Raspberry Pi-
	- ![[Pasted image 20231011111614.png|100x100]]
	- This will be the component we use to turn input from the user into sound.

# Building the Circuit
## Circuit part 1 - Setting up the touch sensor
- ![[Pasted image 20231012091746.png|400x300]] 
- To create this circuit start off by making sure that your breadboard and your T-Cobbler Plus - GPIO Breakout are connected and ready to go. Then start by getting 3 female to male wires. Use the female end of the wires to connect it to the sensor itself by using the 3 prongs on the sensor. Then connect the male end of the wires to the corresponding pins on the breadboard as shown above.
- And that's part one complete, now make some room for part two as we will be doing a very similar process just on the left side of the Cobbler.
## Circuit part 2 - Setting up the buzzer.
- ![[Pasted image 20231012093309.png|400x300]]
- To create the second half of the circuit make sure that the sensor half of the circuit is still intact and begin the same process but for the buzzer.
- Connect the female ends of the wires to the buzzer itself via the prongs. Then connect the male end wires to their corresponding places on the breadboard as shown above.
- You can see that I put a piece of tape on my buzzer. That was because I wanted to make the buzzer quieter but don't worry about that because we will change the frequency of the buzzer in our code.
- But now your circuit is complete. Make sure that both parts are still intact and that there are no loose pins.
- Turn your Pi on and we will implement the Python script.
