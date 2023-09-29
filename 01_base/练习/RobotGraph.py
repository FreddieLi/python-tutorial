"""
Given a 6x6 grid matrix, Robot is given the knowledge of Grid Occupancy Mapping, current location, and the destination as illustrated below:
Current robot's location is at (1, 3), destination is at (6, 2), and the occupied cells are (3,2),(3,3),(3,4),(4,2),(4,3),(4,4).
Write a solution class to search for a navigable path from current location to the destination, 
and validate your solution against the illustrated sample in the main() function.

Note that the robot can only move to adjacent cells either vertically or horizontally but not diagonally!
"""
# This answer is from chatGPT.  
from collections import deque

class RobotGrid:
    def __init__(self, grid_size, occupied_cells, current_location, destination):
        self.grid_size = grid_size
        self.occupied_cells = set(occupied_cells)
        self.current_location = current_location
        self.destination = destination

    def is_valid(self, x, y):
        return 1 <= x <= self.grid_size[0] and 1 <= y <= self.grid_size[1] and (x, y) not in self.occupied_cells

    def find_path(self):
        visited = set()
        queue = deque([(self.current_location, [])])

        while queue:
            current, path = queue.popleft()
            x, y = current

            if current == self.destination:
                return path + [current]

            if current in visited:
                continue

            visited.add(current)

            # Generate possible moves (up, down, left, right)
            moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for move in moves:
                if self.is_valid(*move):
                    queue.append((move, path + [current]))

        return None  # No path found

def main():
    grid_size = (6, 6)
    occupied_cells = [(3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)]
    current_location = (1, 3)
    destination = (6, 2)

    robot = RobotGrid(grid_size, occupied_cells, current_location, destination)
    path = robot.find_path()

    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
