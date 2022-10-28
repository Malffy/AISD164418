def power(number: int, n: int) -> int:
    if n < 1:
        return 1
    if n < 2:
        return number
    if n < 3:
        return number*number
    else:
        return number*power(number, n - 1)


print(power(5, 2))
