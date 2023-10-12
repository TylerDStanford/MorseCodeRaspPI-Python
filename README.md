# MorseCodeRaspPI-Python
Turn both touch input from a sensor and keyboard input from a user and turn it into morse code via a buzzer on your Raspberry Pi.

# Materials List:
- Raspberry Pi-
	-![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/d8ae4ce2-6f92-474e-8a72-6a09a1a513c9)
	- This will be the mini computer you connect your circuits to and run your python scripts on.
- A T-Cobbler Plus - GPIO Breakout
	- ![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/08be5423-7290-4736-911f-17a75daf9d67)
	- I use this to make the connection of circuits to my Pi via the breadboard easier. You don't absolutely need this but it may be hard to follow my tutorial without it.
- Breadboard -
	- ![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/3809620c-9af0-437e-9236-3d458efee07c)
	- This will be the means you use to connect the circuits to your Raspberry Pi. This is a non-permanent way to make circuits for your Pi.
- 1x Touch Module -
	- ![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/545d7f64-1e4d-4bb9-86f2-05679ec3209f)
	- This is the touch sensor we will be using to receive touch input from our user. 
- 6x Female to Male Jumper Cables-
	- ![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/668f4f07-f096-42ce-962c-f82ba2d618d4)
	- These 6 cables are going to be used to connect your touch sensor and your buzzer to your Pi via the breadboard.
- 1x Active Buzzer (white sticker)Raspberry Pi-
	- ![image](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/17f44cac-8ef3-43db-af84-060480a2d26c)
	- This will be the component we use to turn input from the user into sound.

# Building the Circuit
## Circuit part 1 - Setting up the touch sensor
- ![Screenshot from 2023-10-12 09-17-37](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/e9fd6ce3-758b-479d-89d5-f578ded19472)
- To create this circuit start off by making sure that your breadboard and your T-Cobbler Plus - GPIO Breakout are connected and ready to go. Then start by getting 3 female to male wires. Use the female end of the wires to connect it to the sensor itself by using the 3 prongs on the sensor. Then connect the male end of the wires to the corresponding pins on the breadboard as shown above.
- And that's part one complete, now make some room for part two as we will be doing a very similar process just on the left side of the Cobbler.
## Circuit part 2 - Setting up the buzzer.
- ![Screenshot from 2023-10-12 09-32-45](https://github.com/TylerDStanford/MorseCodeRaspPI-Python/assets/141964312/edb75f95-72cd-4d53-ae62-62c783138d8b)
- To create the second half of the circuit make sure that the sensor half of the circuit is still intact and begin the same process but for the buzzer.
- Connect the female ends of the wires to the buzzer itself via the prongs. Then connect the male end wires to their corresponding places on the breadboard as shown above.
- You can see that I put a piece of tape on my buzzer. That was because I wanted to make the buzzer quieter but don't worry about that because we will change the frequency of the buzzer in our code.
- But now your circuit is complete. Make sure that both parts are still intact and that there are no loose pins.
- Turn your Pi on and we will implement the Python script.
