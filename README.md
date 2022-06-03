Note: The source code can be found by navigating through the WoodWindInstrument folder (WoodWindInstrument > project > instrument.py) 

# Table of Content
- [Table of Content](#table-of-content)
- [Description of the machine](#description-of-the-machine)
- [How it works](#how-it-works)

# Description of the machine
The system consists of a BrickPi, a battery pack, a small speaker, a EV3 Touch sensor, an EV3 Ultrasonic Sensor, Lego pieces and a few other parts distributed by the University. The structure was made by keeping in mind that the BrickPi and the battery pack should not fall out of the instrument as this might damage the hardware. The Touch Sensor and the Ultrasonic Sensor were connected to ports 1 and 2 of the BrickPi respectively. To ensure that the sensors do not disconnect from the BrickPi or dangle around, they were both fixed onto the structure of the instrument using the materials provided by the University. Finally, the small speaker was connected onto the audio jack of the BrickPi and just like the sensors, it was also fixed onto the structure of the instrument. A representation of the entire instrument can be seen in Figure 1.  

<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/WoodWindInstrument/main/Picture/Figure%201.PNG" width="300" height="400" />
</p>
<p align="center">
Figure 1 : Picture of the entire system
</p>

# How it works
Overall , the system is designed to play musical notes based on the distance between the users' hands and the Ultrasonic sensor mounted on the musical instrument. The instrument begins reading data from the Ultrasonic sensor once the Touch sensor is pressed. When the Ultrasonic sensor reads a value in the range ] -∞ , 0 [ and ] 40 , ∞ [ the instrument will not play any musical notes. When the Ultrasonic sensor reads a value in the range [0,40], the instrument will play the appropriate musical note. Precisely, when it reads a value in the range [0,10] it will play E4, when it reads a value in the range [10,20] it will play A4, when it reads a value in the range [20,30] it will play F4, and when it reads a value in the range [30,40] it will play B4. The note selection subsystem can be summarized by Figure 2. After the user presses the Touch Sensor again, the Ultrasonic sensor stops reading data and as a consequence the instrument will stop playing musical notes. The user can keep turning on and turning off the instrument at will.

<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/WoodWindInstrument/main/Picture/Figure%202.PNG" width="700" height="200" />
</p>
<p align="center">
Figure 2 : Picture of the note selection subsystem where Note #1 is E4 , Note #2 is A4 , Note #3 is F4 and Note #4 is B4
</p>



## Project Organization

In this section, we go over the files and folders included in this project
listed in alphabetical order.

- `lib`: contains libraries used by the robot such as
  the simpleaudio sound library.
- `project`: all Python files in this folder run on the robot.
  - [`doc`](project/doc): documentation for the brick API
  (Application Programming Interface)
  - [`utils`](project/utils): brick-related utilities for this project.
    - `brick.py`: the main module for interacting with the brick hardware.
    - `sound.py`: module that allows you to play sounds.
    It depends on the simpleaudio library.
  - [**`instrument.py`**](project/instrument.py):
  **Implement your instrument in this file.** You may use other files,
  but you do not need to. Complete the items marked with `TODO`, then
  remove the `TODO`s when you are done.
- `scripts`:
  - `reset_brick.py`: If your program does not exit correctly, eg,
  if you are stuck in an infinite loop, run this script on the brick to reset it.
- `deploy_to_robot.py`: a script to deploy the code to the robot from your computer.
  It offers the following options:
  - Deploy DPM Project on Robot without running:
  copy the `lab3` folder to the robot.
  - Deploy and run DPM Project on Robot:
  copy the `lab3` folder to the robot and run the file specified
  in `project_info.json`.
  - Reset Robot: reset the robot.
- **`project_info.json`**: a file containing information about the project.
- `robot_setup.sh`: a script to install the simpleaudio library on
the brick as described above.

# References 
Special thanks to the TA's and the Professors from the course Design Principles and Methods in Winter 2022 for providing the WoodWindInstrument folder and everything necessary for completing this project. 
