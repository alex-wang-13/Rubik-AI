class Node:
    """
    A class to represent a Node in the search tree.

    Attributes:
        state_str (str): A string representation of the in-order numbers in this Node.

        goal_state (list[list[int]]): The goal state of the Node.
    """
    goal_state: list[list[int]] = [
              [0, 0],
              [0, 0],
        [1, 1, 2, 2, 3, 3, 4, 4],
        [1, 1, 2, 2, 3, 3, 4, 4],
              [5, 5],
              [5, 5]
    ]

    def __init__(self,
                 state: list[list[int]],
                 parent: "Node" = None,
                 action: str = None,
                 path_cost: int = 0) -> None:
        """
        A constructor for this Node.

        Parameters:
            state (list[list[int]]): The state of the puzzle.

            parent (Node): The Node from which this Node was generated (if applicable).

            action (str): The action that was performed on the parent Node to generate this Node (if applicable).

            path_cost (int): The total cost of the path from the initial state to this Node.
        """
        
        self.state: list[int] = state
        self.action: str = action
        self.parent: Node = parent
        self.path_cost: int = path_cost
        self.state_str: str = "".join([str(n) for n in state])

    def __hash__(self) -> int:
        return hash(self.state_str)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.state_str == other.state_str
        return False
    
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.state_str < other.state_str
        raise TypeError("Cannot compare Node with non-Node object")

    def misplaced_tiles(self) -> int:
        """
        A function to calculated the number of misplaced faces on the cube.
        
        Returns:
            int: The number of misplaced faces.
        """

        count: int = 0
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                if self.goal_state[i][j] != value:
                    count += 1

        return count