def fib(i: int) -> int:
    """
    The function receives an index of the fibonacci sequence and returns its value.
    @param i: index in fibonacci sequence.
    @return: value of the sequence in index i.
    """
    if i < 2:  # if i is 0 or 1, which is first two places in sequence
        return i  # return i, which is 0 or 1.
    else:
        return fib(i-2)+fib(i-1)  # return two values before it


def func_run_time():
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))


def fib2(i: int) -> int:
    x_0 = 0
    x_1 = 1
    x_2 = 0
    for j in range(i-1):
        x_2 = x_0 + x_1
        x_0 = x_1
        x_1 = x_2
    return x_2


def main():
    # print(fib(43))
    print(fib2(43))


def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


if __name__ == "__main__":
    # func_run_time()
    print(Towers(4, 'P1', 'P2', 'P3'))

