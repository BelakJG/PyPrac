step = 1
def solve(num_rings, origin = "A", dest = "C", aux = "B"):
    global step
    if num_rings == 1:
        print(f"{step}: Move ring {origin} to {dest}")
        step += 1
        return
    solve(num_rings - 1, origin, aux, dest)
    print(f"{step}: Move ring {origin} to {dest}")
    step += 1
    solve(num_rings - 1, aux, dest, origin)

n = int(input("How many rings to solve for? "))
solve(n)