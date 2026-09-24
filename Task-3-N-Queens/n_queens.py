def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


def main():
    n = int(input("Enter the value of N: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print("\nSolution:\n")
        print_board(board)
    else:
        print("No solution exists for N =", n)


if __name__ == "__main__":
    main()