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
Overall , the system is designed to play musical notes based on the distance between the users' hands and the Ultrasonic sensor mounted on the musical instrument. The instrument begins reading data from the Ultrasonic sensor once the Touch sensor is pressed. When the Ultrasonic sensor reads a value in the range ] -∞ , 0 [ and ] 40 , ∞ [ the instrument will not play any musical notes. When the Ultrasonic sensor reads a value in the range [0,40], the instrument will play the appropriate musical note. Precisely, when it reads a value in the range [0,10] it will play E4, when it reads a value in the range [10,20] it will play A4, when it reads a value in the range [20,30] it will play F4, and when it reads a value in the range [30,40] it will play B4. The note selection subsystem can be summarized by Figure 2. After the user presses the Touch Sensor again, the Ultrasonic sensor stops reading data and as a consequence the instrument will stop playing musical notes.The user can keep turning on and turning off the instrument at will.

<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/WoodWindInstrument/main/Picture/Figure%202.PNG" width="700" height="200" />
</p>
<p align="center">
Figure 2 : Picture of the note selection subsystem where Note #1 is E4 , Note #2 is A4 , Note #3 is F4 and Note #4 is B4
</p>


# What was learned 
# Difficulties

