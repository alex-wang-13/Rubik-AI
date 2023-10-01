import heapq
import math
import random

from node import Node
from typing import Callable

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
    MOVE_SET: list[str] = ["f", "u", "r", "f'", "u'", "r'"]

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
        self.max_nodes: int = math.inf

    def reset(self) -> None:
        """
        A function to reset the state of the cube to its default state.
        """

        self.state = self.DEFAULT_STATE

    def print_state(self) -> None:
        """
        A function to print the current state of the puzzle.
        """

        f_str: str = f"      {self.state[0]}\n      {self.state[1]}\n{self.state[2]}\n{self.state[3]}\n      {self.state[4]}\n      {self.state[5]}\n"
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
                self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][1], self.state[4][1], self.state[3][3]\
                    = self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][1], self.state[4][1], self.state[3][3], self.state[2][3], self.state[1][1]
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
                self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][1], self.state[4][1], self.state[3][3]\
                    = self.state[4][1], self.state[3][3], self.state[2][3], self.state[1][1], self.state[0][1], self.state[2][6], self.state[3][6], self.state[5][1]
            case _:
                raise ValueError(f"The move {move} has not been implemented.")

    def shuffle(self, n: int | str) -> None:
        """
        A function to shuffle the cube randomly n times.

        Parameters:
            n (int | str): A value representing the number of times the cube
            will be shuffled.
        """

        # Setting the seed (for consistency in testing).
        random.seed("axw582")
        for _ in range(int(n)):
            self.move(random.choice(self.MOVE_SET))

    def is_default_goal(self) -> bool:
        """
        A function to check if the current state of the cube is the goal state.
        """

        return self.state == self.DEFAULT_GOAL
    
    def expand(self, node: Node) -> list[Node]:
        """
        A function to expand a particular Node.
        
        Returns:
            list[Node]: A list of child Nodes.
        """

        children: list[Node] = []
        curr_state: list[list[int]] = self.state.copy()
        for move in self.MOVE_SET:
            self.move(move)
            children.append(Node(self.state, node, move, node.path_cost+1))
            self.state = curr_state.copy()
        return children
    
    def backtrack(self, node: Node) -> None:
        # Start with initial empty path.
        path: list[str, str] = []

        while node:
            # Add the node + subsequent action.
            path.append((node.state_str, node.action))
            # Update the current Node.
            node = node.parent

        print( len(path), "".join(path) )

    def solve_astar(self) -> None:
        """
        A function to search for the goal state with A* search.
        """

        # Define the initial Node.
        node: Node = Node(self.state.copy())
        # Declare the frontier.
        frontier: list[Node] = []
        heapq.heappush(frontier, (0, node))
        # Track closed states.
        closed_set: set[Node] = set()

        # Store the Nodes' cheapest cost.
        g_score: dict[Node, int] = dict()
        g_score[node] = 0
        node.path_cost = 0
        # Store the Nodes' evaluation.
        f_score: dict[Node, int] = dict()
        f_score[node] = node.misplaced_tiles() + 0

        # Track the number of Nodes considered.
        n_count: int = 0
        while len(frontier) > 0:
            # Pop the highest priority Node.
            node: Node = heapq.heappop(frontier)[1]
            # Check if the Node is already closed.
            if node in closed_set:
                continue
            else:
                closed_set.add(node)
            # Check + update the number of nodes considered.
            if n_count < self.max_nodes:
                n_count += 1
            else:
                print(f"Exceeded limit for nodes considered: {self.max_nodes}.")
                break

            # Check if the goal is reached.
            if self.is_default_goal():
                return self.backtrack(node)
            
            # For each child node.
            for child in self.expand(node):
                # Add path cost up to child node to the tentative score.
                tentative_score: int = g_score.get(node, math.inf) + 1
                # Check if there is an improvement in path cost.
                if child not in g_score or tentative_score < g_score[child]:
                    # Update tables.
                    child.parent = node
                    g_score[child] = tentative_score
                    f_score[child] = tentative_score + child.misplaced_tiles()
                    if child not in frontier:
                        heapq.heappush(frontier, (f_score[child], child))

        print( "FAILURE" )