# 0 3 5 10
# 0 +3; 3+2; 5+3; 8+2
# +3, +2, +3, +2
def nums(n: int):
    i = 0
    print(i)
    while i < n:
        i += 3
        print(i)
        i += 2
        print(i)


def main():
    nums(700)


if __name__ == "__main__":
    main()
