from logger.log import log
import json
import logging

logging.basicConfig(level=logging.DEBUG)
# format='[%(levelname)s]: %(message)s (@%(name)s)')  

with open("data_preservation/data.json", "r") as jsfile:
    CONTACTS = json.load(jsfile)

class ExitPhonebook(Exception):
    pass

def execute(cmd: list[str]):
    match cmd:
        case ['ls']: print(CONTACTS)

        case ['ls', name]:
            # if name =="":
            #     raise TypeError()

            assert name != ""

            print(CONTACTS.get(name.capitalize(), "Not found!"
        ))

        case ['add', name, info]: CONTACTS[name.capitalize()] = info

        case ['del' | 'rm', name]: 
            name = name.capitalize()

            if name in CONTACTS:
                info = CONTACTS.pop(name)
                # print(f"Removed {info} of {name}")
                logging.debug("Removed %s of %s", info, name)
            else:
                # print(f"{name} not found")
                logging.info("%s not found", name)  
                
        case ["quit" | "exit"]: raise ExitPhonebook()

        case [*cmd]:
            # print("Unknown command", cmd)
            logging.warning("Unknown command %s", cmd)

def save_contacts():
    with open("data_preservation/data.json", "w") as jsfile:
        json.dump(CONTACTS, jsfile)

# Main loop

log("Phonebook", decor="#", padding=3)

# execute(["ls", ""])

while True:
    try:
        cmd = input("> ")
        exit_code = execute(cmd.split())

    except ExitPhonebook:
        save_contacts()
        break

    except Exception:
        # print("Some errors occurred")
        logging.error("Some error occurred")