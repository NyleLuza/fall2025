"""
#  1
def promising(board, row, col):
    # Check column and diagonals
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if len(solutions) == 2:  # stop after 2 solutions
            return

        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if promising(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


# Run for n = 6 and n = 7
print("Solutions for n = 6:")
print(solve_n_queens(6))

print("\nSolutions for n = 7:")
print(solve_n_queens(7))


Solutions for n = 6:
[[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3]]

Solutions for n = 7:
[[0, 2, 4, 6, 1, 3, 5], [0, 3, 6, 2, 5, 1, 4]]



# 2
print("\nSolutions for n = 8:")
print(solve_n_queens(8))
Solutions for n = 8:
[[0, 4, 7, 5, 2, 6, 1, 3], [0, 5, 7, 2, 6, 3, 1, 4]]


# 3

def promising(x, k):
    # Check if queen in row k is safe
    for i in range(1, k):
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return False
    return True


def expand(x, k, n, solutions):
    if promising(x, k):
        if k == n:
            # Found a full solution
            solutions.append(x[1:].copy())   # store solution (ignore index 0)
        else:
            for col in range(1, n + 1):
                x[k + 1] = col
                expand(x, k + 1, n, solutions)


def n_queens(n):
    x = [0] * (n + 1)       # x[1..n], ignore index 0
    solutions = []
    expand(x, 0, n, solutions)
    return solutions


print("\nSolutions for n = 4:")
sols = n_queens(4)
print(sols)

#4
155 nodes need to be checked because then we would just be 
iterating through each possible node until it reaches a dead end
"""