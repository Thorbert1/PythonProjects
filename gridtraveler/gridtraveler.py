import time


def gridtraveler1(m, n, memo):
    if f"{m},{n}" in memo or f"{n},{m}" in memo:
        return memo[f"{m},{n}"]
    if m == 1 or n == 1:
        return 1
    memo[f"{m},{n}"] = memo[f"{n},{m}"] = gridtraveler1(m - 1, n, memo) + gridtraveler1(
        m, n - 1, memo
    )

    return memo[f"{m},{n}"]


def gridtraveler2(m, n, memo):
    if f"{m},{n}" in memo:
        return memo[f"{m},{n}"]
    if m == 1 or n == 1:
        return 1
    memo[f"{m},{n}"] = gridtraveler2(m - 1, n, memo) + gridtraveler2(m, n - 1, memo)

    return memo[f"{m},{n}"]


def main():
    start1 = time.time()
    gridtraveler1(300, 300, memo={})
    end1 = time.time()

    start2 = time.time()
    gridtraveler2(300, 300, memo={})
    end2 = time.time()

    print(
        f"Extra optimized ver = {end1 - start1:.7}s\nNon optimized ver = {end2 - start2:.7}s"
    )


if __name__ == "__main__":
    main()
