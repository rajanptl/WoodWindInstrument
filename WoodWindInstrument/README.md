# Lab 3 - Mini-Project

_Read this entire document before doing anything._

In this lab, we will test the robot sensors to learn how they can be used in an
application, eg, a musical instrument.
For lab objectives, demo and report requirements, submission instructions, and
deadlines, see detailed instructions on MyCourses.

If you need help, please post on the discussion board or contact your
mentor TA.

## Updates and corrections

We will post any updates, corrections, and
clarifications to the starter code or these instructions on
[this page](https://mcgill-dpm.github.io/website/Corrections).
Please check it regularly.

## Software requirements

- The software implementation must be done in Python 3.9 or higher
- You are allowed to create extra files, classes, and functions,
  but you must not alter the project structure
- The use of any external software libraries not included with the BrickPi or
  the lab materials requires prior approval from the course staff

## Setup

As with the previous lab, you will have two options for developing code for the robot:

- **Option 1: Simple Setup.** With this option, you will work on the robot directly,
using NoMachine and Thonny.
This is the recommended approach for beginners since the setup is simpler.

  Setup instructions for using NoMachine are provided in the
  [Getting Started Guide](https://mcgill-dpm.github.io/website/GettingStarted#connecting-to-the-brick).
  Once you have connected to the robot, use a private browsing window to go to
  [MyCourses](https://mycourses2.mcgill.ca/d2l/home/556943) and download
  the zip file containing the starter code to the `ecse211` folder.
  Right-click on the zip file and select "Extract Here".

  When you are ready to submit your code, right-click on the `Lab3` folder
  and select "Compress" and pick a location to save the zip file.
  Upload the zip file to the Lab 3 submission folder on MyCourses.

- **Option 2: Flexible Setup.** With this option, you develop your code in an advanced
IDE such as VS Code on your computers and send it to the robot.
This is recommended for more experienced students as it offers greater flexibility,
since all three members can work on the lab in parallel.
Setup details for this option are provided [here](flexible-setup.md).

  You still need to submit a zip file of your code to the Lab 3 submission folder
  on MyCourses. You can create the zip file on the robot as described in
  "Option 1" above, or simply download the zip file from GitHub (make sure
  you committed and pushed all your changes first!). 

If you are unsure which option to choose, pick Option 1.
If you have issues with NoMachine, contact your mentor TA for assistance, and
consider Option 2 as a backup option.

___

**In both cases, also do the following:**

**On the brick:** Double-click `robot_setup.sh` and select "Run in terminal"
to install the necessary libraries.

___

## Project Organization

In this section, we go over the files and folders included in this lab,
listed in alphabetical order.
The files you need to modify are shown in **bold**.

- `lib`: contains libraries used by the robot such as
  the simpleaudio sound library.
- `project`: all Python files in this folder run on the robot.
  - [`doc`](project/doc): documentation for the brick API
  (Application Programming Interface), ie, the classes and functions
  you can use to work with the robot.
  - [`utils`](project/utils): brick-related utilities for this project.
  See the other project files to see examples of how to use these modules.
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

