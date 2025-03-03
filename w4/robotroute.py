# not submitted solution


def analyze_route(grid):
    # Find starting position
    rows = len(grid)
    cols = len(grid[0])
    start_row = start_col = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'R':
                start_row, start_col = i, j
                break

    # Directions: 0=up, 1=right, 2=down, 3=left
    # dx and dy represent the change in position for each direction
    dx = [0, 1, 0, -1]  # column changes
    dy = [-1, 0, 1, 0]  # row changes

    visited = set()  # Track visited positions
    visited.add((start_row, start_col))

    # Current position and direction
    row, col = start_row, start_col
    direction = 0  # Start moving up

    # Track positions+directions to detect loops
    state_history = set()
    state_history.add((row, col, direction))

    while True:
        # Calculate next position
        new_row = row + dy[direction]
        new_col = col + dx[direction]

        # Check if robot exits grid
        if (new_row < 0 or new_row >= rows or
                new_col < 0 or new_col >= cols):
            return len(visited), True

        # Check for obstacle
        if grid[new_row][new_col] == '#':
            # Turn right
            direction = (direction + 1) % 4
            # If we've seen this state before, it's a loop
            if (row, col, direction) in state_history:
                return len(visited), False
            state_history.add((row, col, direction))
        else:
            # Move to new position
            row, col = new_row, new_col
            visited.add((row, col))
            # If we've seen this state before, it's a loop
            if (row, col, direction) in state_history:
                return len(visited), False
            state_history.add((row, col, direction))


if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1))  # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2))  # (12, False)
