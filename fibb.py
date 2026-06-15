rec_calls = 0

def fibb(n):
    def fibb_tail(n, a=0, b=1):
        global rec_calls
        if n == 0:
            return a
        if n == 1:
            return b
        rec_calls += 1
        return fibb_tail(n - 1, b, a + b)

    return fibb_tail(n)

if __name__ == "__main__":
    n = 20
    print(f"{n}th fibb: {fibb(n)}, recursion calls: {rec_calls}")