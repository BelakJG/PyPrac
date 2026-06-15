step = 1
def solve(n, origin = "A", dest = "C", aux = "B"):
    global step
    if n == 0:
        return
    solve(n-1, origin, dest, aux)
    print(f"Step {step}: Move {origin} to {aux}")
    step += 1
    solve(n-1, dest, origin, aux)
    print(f"Step {step}: Move {aux} to {dest}")
    step += 1
    solve(n-1, origin, dest, aux)

if __name__ == "__main__":
    solve(3)