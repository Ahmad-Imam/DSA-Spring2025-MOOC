
def dfs(grid_list, r, c):
    if r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]):
        return
    if grid_list[r][c] != '.':
        return

    grid_list[r][c] = '#'

    dfs(grid_list, r - 1, c)
    dfs(grid_list, r + 1, c)
    dfs(grid_list, r, c - 1)
    dfs(grid_list, r, c + 1)


def count_rooms(grid):
    grid_list = []

    for row in grid:
        grid_list.append(list(row))
    answer = 0
    # print(grid)
    # print(grid_list)

    for r in range(len(grid_list)):
        for c in range(len(grid_list[0])):
            if grid_list[r][c] == '.':
                # print("Found a room at", r, c)
                answer += 1
                dfs(grid_list, r, c)

    return answer


if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid))  # 4

    # grid = ["########",
    #         "#......#",
    #         "#.####.#",
    #         "#......#",
    #         "########"]
    # print(count_rooms(grid))  # 1

    # grid = ["########",
    #         "######.#",
    #         "##.#####",
    #         "########",
    #         "########"]
    # print(count_rooms(grid))  # 2
