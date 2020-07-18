#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event2')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308
lBump = 310
rBump = 311
lStick = 317
rStick = 318
menu = 315
windows = 158
bigX = 0

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == xBtn:
                print("X")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                print("A")
            elif event.code == yBtn:
                print("Y")
            elif event.code == lBump:
                print("LEFT Bumper")
            elif event.code == rBump:
                print("RIGHT Bumper")
            elif event.code == lStick:
                print("Right Joystick")
            elif event.code == rStick:
                print("Right Joystick")
            elif event.code == menu:
                print("Menu")
            elif event.code == windows:
                print("Widnows")
        elif event.value == 0:
          print("Relache | Release")

    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":#0
             print("Left Joystick xPos = " + str((absevent.event.value-32767)/32767))
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":#1
             print("Left Joystick yPos = " + str((absevent.event.value-32767)/32767))
        
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#2
             print("Right Joystick xPos = " + str((absevent.event.value-32767)/32767))
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":#5
             print("Right Joystick yPos = " + str((absevent.event.value-32767)/32767))
        
        
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":#16
            if absevent.event.value == 1:
                 print("Right dPad")
            elif absevent.event.value == -1:
                 print("Left dPad")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":#17
            if absevent.event.value == 1:
                 print("Down dPad")
            elif absevent.event.value == -1:
                 print("Up dPad")
        
        
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_GAS":#9
            print("RT " + str(absevent.event.value/1023))
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_BRAKE":#10
            print("LT " + str(absevent.event.value/1023))