from logger.log import log
import json

with open("data_preservation/data.json", "r") as jsfile:
    CONTACTS = json.load(jsfile)

def execute(cmd: list[str]):
    match cmd:
        case ['ls']: print(CONTACTS)

        case ['ls', name]: print(CONTACTS.get(name.capitalize(), "Not found!"))

        case ['add', name, info]: CONTACTS[name.capitalize()] = info

        case ['del' | 'rm', name]: 
            name = name.capitalize()

            if name in CONTACTS:
                info = CONTACTS.pop(name)
                print(f"Removed {info} of {name}")
            else:
                print(f"{name} not found")
                
        case ["quit" | "exit"]: return "EXIT"

        case [*cmd]:
            print("Unknown command", cmd)

def save_contacts():
    with open("data_preservation/data.json", "w") as jsfile:
        json.dump(CONTACTS, jsfile)

# Main loop

log("Phonebook", decor="#", padding=3) 

while True:
    cmd = input("> ")
    exit_code = execute(cmd.split())

    if exit_code == "EXIT":
        save_contacts()
        break