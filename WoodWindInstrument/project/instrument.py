from utils import sound
from utils.brick import TouchSensor, EV3UltraSonicSensor, configure_ports
from time import sleep

MUSICAL_NOTE_1 = sound.Sound(duration=0.2, pitch="E4", volume=100)# instantiate a sound instance for the musical note
MUSICAL_NOTE_2 = sound.Sound(duration=0.2, pitch="A4", volume=100)
MUSICAL_NOTE_3 = sound.Sound(duration=0.2, pitch="F4", volume=100)
MUSICAL_NOTE_4 = sound.Sound(duration=0.2, pitch="B4", volume=100)

TOUCH_SENSOR, US_SENSOR = configure_ports(PORT_1=TouchSensor, PORT_2=EV3UltraSonicSensor) # configure ports


def play_note1(): 
    "Play a musical note 1."
    MUSICAL_NOTE_1.play()
    MUSICAL_NOTE_1.wait_done()

def play_note2():
    "Play a musical note 2."
    MUSICAL_NOTE_2.play()
    MUSICAL_NOTE_2.wait_done()

def play_note3():
    "Play a musical note 3."
    MUSICAL_NOTE_3.play()
    MUSICAL_NOTE_3.wait_done()    

def play_note4():
    "Play a musical note 4."
    MUSICAL_NOTE_4.play()
    MUSICAL_NOTE_4.wait_done()

def instrument():
    
    "Plays musical notes based on distance and if touch_status is pressed"
    touch_status=False;#track if the button is pressed
    all_notes = {1:play_note1, 2:play_note2, 3:play_note3, 4:play_note4} #function of dictionaries 
    while True: # infinite loop
        if touch_status: # if button pressed
            if TOUCH_SENSOR.is_pressed():
                touch_status=False #changes the status of button
            print("Instrument ON") # notifies user that the instrument is on
            note=1 # default sound
            us_data = US_SENSOR.get_value() #ultrasonic value
            if us_data >=0 and us_data<10:
                note=1;
            elif us_data >= 10 and us_data<20:
                note=2;
            elif us_data >= 20 and us_data< 30:
                note=3;
            elif us_data >=30 and us_data<40:
                note=4;
            all_notes[note]() #runs specific funciton to play specific note
            sleep(0.25)
            
        else:
            if TOUCH_SENSOR.is_pressed():#checks if button was pressed
                touch_status=True  #changes it to press
            print("Instrument OFF") #notifies user that the instrument is off
            


if __name__ == '__main__':
    instrument()