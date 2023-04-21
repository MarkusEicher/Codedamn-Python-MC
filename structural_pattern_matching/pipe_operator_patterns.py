match input("Are you sure) (y/n): "):
    case "Y" | "y": # Pipe operator used to chain multiple input formats
        print("Yes")
    case "N" | "n": # Pipe operator used to chain multiple input formats
        print("No")
    case cmd:
        print("Invalid input", cmd)


command = input(">>>")

match command.split():

    case ["quit"]:
        print("Bye!")
    
    case ["mkdir", dirname]:
        print(f"Directory {dirname} created")

    case ["ls"]:
        print("Directory contents:")

    case ["ls", ("-l" | "--all" | "-a") as flag]:
        print("Directory contents with more info:\nwith flag", flag)  
    
    case ["ls", dirname]:
        print(f"Listing directory {dirname}...")

    case [cmd, *args]:
        print(f"Unknown command: {cmd}" f" called with args: {args}")
    
