def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    numbers(n - 1)


numbers(10)
