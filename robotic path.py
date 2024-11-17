def is_safe(v, pos, path, n):
    # Check if this vertex is an adjacent vertex of the previously added vertex.
    if pos > 0 and ((abs(path[pos - 1][0] - v[0]) == 1 and path[pos - 1][1] == v[1]) or
                    (abs(path[pos - 1][1] - v[1]) == 1 and path[pos - 1][0] == v[0])):
        return True
    return False


def hamiltonian_circuit_util(n, path, pos, visited):
    # Base case: If all vertices are included in the path
    if pos == n * n:
        return True

    # Try to visit each cell in the grid
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                if is_safe((i, j), pos, path, n):
                    path[pos] = (i, j)
                    visited[i][j] = True

                    if hamiltonian_circuit_util(n, path, pos + 1, visited):
                        return True

                    # Backtrack
                    visited[i][j] = False

    return False


def hamiltonian_circuit(n):
    path = [(-1, -1)] * (n * n)  # Path to store the coordinates
    visited = [[False for _ in range(n)] for _ in range(n)]  # Visited cells

    # Start from the first cell
    path[0] = (0, 0)
    visited[0][0] = True

    if not hamiltonian_circuit_util(n, path, 1, visited):
        return None

    return path


def print_grid_with_path(n, path):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    for step, (x, y) in enumerate(path):
        grid[x][y] = str(step) if step < len(path) - 1 else 'R'  # R for return

    for row in grid:
        print(' '.join(row))


def main():
    # Input the grid size
    n = int(input("Enter the grid size for the robotic path (n x n): "))

    pathway = hamiltonian_circuit(n)

    if pathway:
        print("Hamiltonian Circuit Found!")
        print("----------------------------------------")
        print("Step-by-Step Robot Path:")
        print("----------------------------------------")

        # Print the starting position
        print(f"Starting Position: (0, 0)")

        # Print each step
        for step in range(len(pathway)):
            if step > 0:
                print(f"Step {step}: Move to {pathway[step]}")

        print("----------------------------------------")
        print(f"Final Step: Return to Starting Position {pathway[0]}")
        print("----------------------------------------")

        # Circuit summary
        print("Circuit Summary:")
        print("----------------")
        print(f"- Total Steps: {len(pathway)}")
        print(f"- Starting and Ending Position: {pathway[0]}")
        print(f"- Cells Visited: {pathway}")

        print("\nGrid with the Hamiltonian Path:")
        print_grid_with_path(n, pathway)
    else:
        print("No Hamiltonian Circuit found.")


if __name__ == "__main__":
    main()