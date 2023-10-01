from puzzle_parts import Cube

import sys

def action(command: str, cube: Cube) -> None:
    """
    A function that handles given commands or states a command is not implemented.
    Commands generally follow the format "<command> <a> <b> <c> ..." where the name
    of the command is the first word and more specific instructions related to the
    given command are listed subsequently.

    Parameters:
        command (str): A string representing an action to be performed on a given cube.

        cube (puzzle_parts.Cube): The cube on which to perform an action.
    """

    command: list[str] = command.lower().split()
    
    match command[0]:
        case "shuffle":
            # Give the second argument as input.
            cube.shuffle(command[1])
        case "rotate":
            cube.rotate_sequence(command[1:])
        case "reset":
            cube.reset()
        case "printstate":
            cube.print_state()
        case _:
            # State that a given command is not recognized.
            print(f"The function {command} is not recognized/implemented.")

if __name__ == "__main__":
    # Check for the command file.
    if len(sys.argv) < 2:
        print("No command file provided.")

    # A cube to toy with.
    cube = Cube()

    with open(sys.argv[1]) as file:
        # Run each line in the command file.
        for line in file:
            action(command=line, cube=cube)