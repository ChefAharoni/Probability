import math
from colorama import Back, Fore, Style

UNIT_CIRCLE_DEGREES = {0: {"Sin": 0, "Cos": 1, "Tan": 0},
                       30: {"Sin": (1 / 2), "Cos": (math.sqrt(3) / 2), "Tan": (math.sqrt(3) / 3)},
                       45: {"Sin": (math.sqrt(2) / 2), "Cos": (math.sqrt(2) / 2), "Tan": 1},
                       60: {"Sin": (math.sqrt(3) / 2), "Cos": (1 / 2), "Tan": math.sqrt(3)},
                       90: {"Sin": 1, "Cos": 0, "Tan": ZeroDivisionError},  # Tan = undefined (1/0)
                       120: {"Sin": (math.sqrt(3) / 2), "Cos": -(1 / 2), "Tan": -(math.sqrt(3))},
                       135: {"Sin": (math.sqrt(2) / 2), "Cos": -(math.sqrt(2) / 2), "Tan": -1},
                       150: {"Sin": (1 / 2), "Cos": -(math.sqrt(3) / 2), "Tan": math.sqrt(3)},
                       180: {"Sin": 0, "Cos": -1, "Tan": 0},
                       210: {"Sin": -(1 / 2), "Cos": -(math.sqrt(3) / 2), "Tan": (math.sqrt(3) / 3)},
                       225: {"Sin": -(math.sqrt(2) / 2), "Cos": -(math.sqrt(2) / 2), "Tan": 1},
                       240: {"Sin": -(math.sqrt(3) / 2), "Cos": -(1 / 2), "Tan": math.sqrt(3)},
                       270: {"Sin": -1, "Cos": 0, "Tan": ZeroDivisionError},  # Tan = undefined (-1/0)
                       300: {"Sin": -(math.sqrt(3) / 2), "Cos": (1 / 2), "Tan": -(math.sqrt(3))},
                       315: {"Sin": -(math.sqrt(2) / 2), "Cos": (math.sqrt(2) / 2), "Tan": -1},
                       330: {"Sin": -(1 / 2), "Cos": (math.sqrt(3) / 2), "Tan": math.sqrt(3)},
                       360: {"Sin": 0, "Cos": 1, "Tan": 0}}


def calc_sqrt(a: float, b: float):
    """
    Used this code review to build it -
    https://codereview.stackexchange.com/questions/144041/reduce-square-root-to-simplest-radical-form
    @param a:
    @param b:
    @return:
    """
    ab_squared = (pow(a, 2)) + (pow(b, 2))  # == (a^2) + (b^2)
    r = math.sqrt(ab_squared)
    if r.is_integer():
        return 1, r
    else:
        root = int(math.sqrt(ab_squared))  # Truncates the sqrt of a^2 + b^2
        for factor_root in range(root, 1, -1):  # Checks every number from the truncated root to 1, in negative steps
            factor = factor_root * factor_root  # The number that is being checked if can be sqrt perfectly to be the
            # coefficient before the sqrt symbol; i.e. 9 will be simplified to 3
            if ab_squared % factor == 0:  # If that number can be sqrt perfectly
                reduced = ab_squared // factor  # The number that will be inside the sqrt symbol; i.e. 2
                return factor_root, reduced
        return 1, r


def find_cos_sin_values(cos_t: float, sin_t: float) -> float:
    angle = None
    for k, v in UNIT_CIRCLE_DEGREES.items():
        if cos_t == v["Cos"] and sin_t == v["Sin"]:
            angle = k
    if angle is None:
        return math.atan((sin_t / cos_t)) * (180.0 / math.pi)
    else:
        return angle


def standard_notation():
    # Converts standard notation to trigonometric notation
    # standard = a + bi; trig form = r(cos ϴ + isin ϴ)
    # r = \sqrt{(a^2) + (b^2)}; cos ϴ = {a/r}; sin ϴ = {b/r}
    # stan_form = input("Enter the standard notation: ")  # uncomment
    stan_form = "3 + 3i"
    all_letters = stan_form.split(" ")
    a = float(all_letters[0])
    remove_i = all_letters[2].split("i")
    b = float(remove_i[0])
    r = math.sqrt((pow(a, 2)) + (pow(b, 2)))
    # print("r", r)
    cos_t = a / r
    sin_t = b / r
    # print(cos_t, sin_t)
    angle = find_cos_sin_values(cos_t=cos_t, sin_t=sin_t)
    if type(angle) == int:  # Print angle "as-is"; no decimals.
        print(f'The corresponding angle is - {angle}\u00b0.')  # \u00b0 is degree symbol
    else:  # Print angle with 2 decimals.
        print(f'The corresponding angle is - {angle:.2f}\u00b0.')  # \u00b0 is degree symbol
    print_trig_form(a=a, b=b, angle=angle)


def print_trig_form(a, b, angle: float):
    coefficient, reduced = calc_sqrt(a=a, b=b)
    print("The trig form is - ", end="")
    if coefficient == 1:
        print(f'{int(reduced)}(Cos {angle:.2f}\u00b0 + iSin {angle:.2f}\u00b0)')
    elif reduced == 1:
        print(f'\u221A{coefficient}(Cos {angle}\u00b0 + iSin{angle}\u00b0)')  # \u221A is sqrt symbol
    else:
        print(f'{coefficient}\u221A{reduced}(Cos {angle}\u00b0 + iSin {angle}\u00b0)')  # \u221A is sqrt symbol


def main():
    standard_notation()


if __name__ == "__main__":
    main()
