class Cube:
    """
    A class to represent a 2x2 Rubik's cube.
    """

    DEFAULT_STATE: list[list[int]] = [
              [0, 0],
              [0, 0],
        [1, 1, 2, 2, 3, 3, 4, 4],
        [1, 1, 2, 2, 3, 3, 4, 4],
              [5, 5],
              [5, 5]
    ]

    DEFAULT_GOAL: list[list[int]] = DEFAULT_STATE.copy()

    """
    A set of unique valid moves.
    """
    MOVE_SET: set[str] = {"f", "u", "r", "f'", "u'", "r'"}

    def __init__(self) -> None:
        """
        A function to initialize the cube. The state of the cube is initialized
        as a 6 row numpy array as follows:
        
            0 0
            0 0
        1 1 2 2 3 3 4 4
        1 1 2 2 3 3 4 4
            5 5
            5 5
        
        Each number in the cube represents a distinct color. The 2x2 face of 2s
        are the front of the cube. 
        """

        self.state: list[int] = self.DEFAULT_STATE

    def reset(self) -> None:
        """
        A function to reset the state of the cube to its default state.
        """

        self.state = self.DEFAULT_STATE

    def print_state(self) -> None:
        """
        A function to print the current state of the puzzle.
        """

        f_str: str = f"      {self.state[0]}\n      {self.state[1]}\n{self.state[2]}\n{self.state[3]}\n      {self.state[4]}\n      {self.state[5]}"
        print(f_str)

    def rotate_sequence(self, seq: list[str]):
        """
        A function to perform a sequence of moves.
        
        Parameters:
            seq (list[str]): A sequence of string commands.
        """
        
        for s in seq:
            self.move(s)

    def move(self, move: str) -> None:
        """
        A function to move the cube in a specified direction.
        
        Parameters:
            move (str): The specified move to make.
            
        Raises:
            ValueError: When the specified move is not recognized.
        """

        move = move.strip().lower()
        match move:
            case "f":
                # Clockwise front side.
                # Rotate front face.
                self.state[2][2], self.state[2][3], self.state[3][3], self.state[3][2] = self.state[2][3], self.state[3][3], self.state[3][2], self.state[2][2]
                # Rotate sides.
                self.state[2][1], self.state[1][0], self.state[1][1], self.state[2][4], self.state[3][4], self.state[4][1], self.state[4][0], self.state[3][1]\
                    = self.state[1][1], self.state[2][4], self.state[3][4], self.state[4][1], self.state[4][0], self.state[3][1], self.state[2][1], self.state[1][0]
            case "u":
                # Clockwise upper side.
                # Rotate upper face.
                self.state[0][0], self.state[0][1], self.state[1][1], self.state[1][0] = self.state[0][1], self.state[1][1], self.state[1][0], self.state[0][0]
                # Rotate sides.
                self.state[2] = self.state[2][2:] + self.state[2][:2]
            case "r":
                # Clockwise right side.
                # Rotate right face.
                self.state[2][4], self.state[2][5], self.state[3][5], self.state[3][4] = self.state[2][5], self.state[3][5], self.state[3][4], self.state[2][4]
                # Rotate sides.
                self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][3], self.state[4][3], self.state[3][3]\
                    = self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][3], self.state[4][3], self.state[3][3], self.state[2][3], self.state[1][1]
            case "f'":
                # Counterclockwise front.
                self.state[2][2], self.state[2][3], self.state[3][3], self.state[3][2] = self.state[3][2], self.state[2][2], self.state[2][3], self.state[3][3],
                # Rotate sides.
                self.state[2][1], self.state[1][0], self.state[1][1], self.state[2][4], self.state[3][4], self.state[4][1], self.state[4][0], self.state[3][1]\
                    = self.state[4][0], self.state[3][1], self.state[2][1], self.state[1][0], self.state[1][1], self.state[2][4], self.state[3][4], self.state[4][1]
            case "u'":
                # Counterclockwise upper.
                # Rotate upper face.
                self.state[0][0], self.state[0][1], self.state[1][1], self.state[1][0] = self.state[1][0], self.state[0][0], self.state[0][1], self.state[1][1]
                # Rotate sides.
                self.state[2] = self.state[2][-2:] + self.state[2][:-2]
            case "r'":
                # Counterclockwise right.
                # Rotate right face.
                self.state[2][4], self.state[2][5], self.state[3][5], self.state[3][4] = self.state[3][4], self.state[2][4], self.state[2][5], self.state[3][5]
                # Rotate sides.
                self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][3], self.state[4][3], self.state[3][3]\
                    = self.state[4][3], self.state[3][3], self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][3]
            case _:
                raise ValueError(f"The move {move} has not been implemented.")

    def shuffle(self, n: int | str) -> None:
        """
        A function to shuffle the cube randomly n times.

        Parameters:
            n (int | str): A value representing the number of times the cube
            will be shuffled.
        """

        n: int = int(n)
        # Implement random movement (and don't forget to set the seed).
        pass

    def is_default_goal(self) -> bool:
        """
        A function to check if the current state of the cube is the goal state.
        """

        return self.state == self.DEFAULT_GOAL