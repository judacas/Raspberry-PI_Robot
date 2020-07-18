import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event2')

print(gamepad.active_keys(verbose = False))
print(gamepad.absinfo(0).max)
print(gamepad.absinfo(0).min)