# sandwich number is a number that a number below it is a perfect square root and the number above it is a perfect
# cube root. For example, 26: 25 is a sqrt of 5 and 27 is qbrt of 3.
import math
import gmpy2


def is_square_complicated(pos_int):
    x = pos_int // 2
    seen = {x}  # set of x
    while x * x != pos_int:
        x = (x + (pos_int // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def is_square(pos_int: int):
    is_s = gmpy2.is_square(pos_int)
    if is_s == 0:
        return False
    else:
        return True


def is_qbrt(pos_int: int):
    is_qb = gmpy2.iroot(pos_int, 3)
    if is_qb[1] == 0:
        return False
    else:
        return True


def main():
    import time
    print("Starting...")
    start_time = time.time()
    n = 10000000000000
    sandwich_nums = list()
    for i in range(n):
        # print("Checking for..", i)
        if i-1 < 2:  # skip the first two numbers
            continue
        elif is_square(i-1) and is_qbrt(i+1):
            print("i-1 is", i-1, "its square root is", math.sqrt(i-1))
            print("i is", i)
            print("i+1 is", i+1, "its cube root is", math.cbrt(i))
            sandwich_nums.append(i, (i-1, i+1))
    print("--- %s seconds ---" % (time.time() - start_time))
    return sandwich_nums


def check():
    for i in range(1, 1000001):
        if is_qbrt(i):
            print(i, "\t", math.cbrt(i))

# for i in range(1, 30):
#     print(i, is_square(i))


if __name__ == "__main__":
    main()
    # check()
