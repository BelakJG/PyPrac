from math import sqrt

step = 1
def solve(num_rings, origin = "A", dest = "D", left = "B", right = "C"):
    global step
    if num_rings == 1:
        print(f"{step}: Move ring {origin} to {dest}")
        step += 1
        return

    k = find_k(num_rings)
    solve(k, origin, left, right, dest)
    solve3(num_rings - k, origin, dest, right)
    solve(k, left, dest, origin, right)

def solve3(num_rings, origin, dest, aux):
    global step
    if num_rings == 1:
        print(f"{step}: Move ring {origin} to {dest}")
        step += 1
        return

    solve3(num_rings - 1, origin, aux, dest)
    print(f"{step}: Move ring {origin} to {dest}")
    step += 1
    solve3(num_rings - 1, aux, dest, origin)

def find_k(num_rings):
    return int(num_rings - round(sqrt((2 * num_rings) + 1)) + 1)

n = int(input("Number of rings: "))
solve(n)