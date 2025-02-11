import keyboard as kb
import time
from command_recon import command_recon

hold_commands = set()

def execute_command(command):
    global hold_commands
    if command in ["jump", "dive","grab", "emote"]:
        kb.press_and_release(command_map[command])
    elif command in ["go", "left", "back", "right"]:
        if command not in hold_commands:
            kb.press(command_map[command])
            hold_commands.add(command)
    elif command == "stop":
        for key in hold_commands:
            kb.release(key)
        hold_commands.clear()

command_map = {
    "jump": "space",
    "dive": "ctrl",
    "grab": "shift",
    "emote": "1",
    "go": "w",
    "left": "a",
    "back": "s",
    "right": "d"
}


while True:
    command = command_recon()
    if command:
        print('Command recieved: %s', command)
        execute_command(command)
    else:
        pass
    time.sleep(0.5)