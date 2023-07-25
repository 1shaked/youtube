

def amountOfCarsCanPark(n: int):
    if (n == 0 or n == 1):
        return 0
    count = 1
    for i in range(0, n-1):# from zero up to n-2 inclusive
        count += (1/(n-1)) * (amountOfCarsCanPark(i) + amountOfCarsCanPark(n - i-2))
    return count

print(amountOfCarsCanPark(20))