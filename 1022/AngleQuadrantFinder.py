import math
from colorama import Back, Fore, Style

# The Match statement docs -  https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
# Taken from Math 1022, LSUE.

SPECIAL_FUNC_VALS = {30: {"Sin": (1 / 2), "Cos": (math.sqrt(3) / 2), "Tan": (math.sqrt(3) / 3)},
                     45: {"Sin": (math.sqrt(2) / 2), "Cos": (math.sqrt(2) / 2), "Tan": 1},
                     60: {"Sin": (math.sqrt(3) / 2), "Cos": (1 / 2), "Tan": math.sqrt(3)}}


def axis_nums(x: float) -> str | float:
    """
    After the number is reduced by 360 until it is smaller than 360 - check if it is on the axis of the numbers. Checks
    negative numbers as well.
    @param x: Angle less than 360 that is being checked.
    @return: axis the angle is on; returns x unchanged if x isn't on axis.
    """
    match x / 360:
        case 1 | -1:
            return "axis; I"
        case .25 | -.75:
            return "axis; II"
        case .5 | -.5:
            return "axis; III"
        case .75 | -.25:
            return "axis; IV"
        case default:
            return x


def find_pos_angle(x: float) -> float:
    """
    A completion function to find_neg_quad; returns the reference angle and print every step of the division.
    @param x: Angle to be checked.
    @return: Reference Angle
    """
    while x > 360:
        print(f'{x} - 360 = ', end="")
        x -= 360
        print(x)
    return x


def find_pos_quad(x1: float) -> str:
    """
    If angle (x) is positive, subtracts 360 from it until it is less than 360. Then, checks if number is on the axis
    by calling axis_nums on x; if it is - returns x; otherwise: checks the truncated number left from dividing by 90
    to check what quadrant the angle is on.
    Method used from this site -
    https://study.com/skill/learn/how-to-determine-the-quadrant-given-an-angle-in-degrees-explanation.html
    @param x1: Angle to be checked.
    @return: Quadrant or axis x is on.
    """
    x = find_pos_angle(x1)
    y = axis_nums(x)
    if y == x:
        print(f'{x} / 90 = ', end="")
        x //= 90  # actually floor division can work the same way
        print(f'{x:.4f}\n')
        match x:
            case 0:
                return "I"
            case 1:
                return "II"
            case 2:
                return "III"
            case 3:
                return "IV"
            case default:
                raise ValueError
    else:
        return y


def find_neg_angle(x: float) -> float:
    """
    A completion function to find_neg_quad; returns the reference angle and print every step of the division.
    @param x: Angle to be checked.
    @return: Reference Angle
    """
    while x < -360:
        print(f'{x} - 360 = ', end="")
        x += 360
        print(x)
    return x


def find_neg_quad(x1: float) -> str:
    """
    If angle (x) is negative, adds 360 from it until it is bigger than -360. Then, checks if number is on the axis
    by calling axis_nums on x; if it is - returns x; otherwise: checks the truncated number left from dividing by 90
    to check what quadrant the angle is on.
    Method used from this site -
    https://study.com/skill/learn/how-to-determine-the-quadrant-given-an-angle-in-degrees-explanation.html
    @param x1: Angle to be checked.
    @return: Quadrant or axis x is on.
    """
    x = find_neg_angle(x1)
    y = axis_nums(x)
    if y == x:
        print(f'{x} / 90 = ', end="")
        x //= 90
        print(f'{x:.4f}\n')
        match x:
            case 0:
                return "IV"
            case -1:
                return "III"
            case -2:
                return "II"
            case -3:
                return "I"
            case default:
                raise ValueError
    else:
        return y


def check_num(x: float) -> str:
    """
    Checks if x is directly a divisible of 360, thus it is on the axis. If so, returns the axis the angle it's on.
    Otherwise, calls determine_sign to check if x is negative or positive - and then return the quadrant x is on.
    @param x: Angle to be checked
    @return: Quadrant or axis x is on. (quadrant is determined by find pos/neg quad)
    """
    print(f'{x} % 360 = {x % 360}\n')
    match x % 360:
        case 0:
            return "axis; I"
        case .25 | -.25:
            return "axis; II"
        case .5 | -.5:
            return "axis; III"
        case .75 | -.75:
            return "axis; IV"
        case default:
            return determine_sign(x)


def determine_sign(x: float) -> str:
    """
    Checks the sign of x. If positive - calls find_pos_quad; if negative (else) - calls find_neg_quad. Eventually they
    will return the Quadrant or axis x is on.
    @param x: Angle to be checked
    @return: Quadrant or axis x is on. (quadrant is determined by find pos/neg quad)
    """
    if x > 0:
        q = find_pos_quad(x)
        return q
    else:
        q = find_neg_quad(x)
        return q


def convert_angle(x: float, a_type: str) -> float:
    """
    Converts an angle from radians to degrees and vice versa.
    @param x: Angle to convert.
    @param a_type: Conversion needed
    @return: Converted angle
    """
    a_type = a_type.lower().title()
    if a_type == "Radians" or a_type.startswith("Rad"):
        # Convert Radians to Degrees
        d = x * (180 / math.pi)
    elif a_type == "Degrees" or a_type.startswith("Deg"):
        # Convert Degrees to Radians
        d = x * (math.pi / 180)
    else:
        raise ValueError
    return d


def ref_angle(x: float) -> float:
    """
    Checks the reference angle for the checked angle.
    @param x: Angle to be checked.
    @return: Reference angle
    """
    return x % 360


def main() -> None:
    # angle_type = input("What is your angle mode? (Radians/Degrees)\n>>> ")
    # There is a problem here since I haven't considered multiple runs.
    # Besides, not sure the calculation works with radians.

    # Add in the results the value of the angle in the form of: Cos ϴ = x; Sin ϴ = y
    deg = input("Enter your degree: ")
    # d = convert_angle(x=float(deg), a_type=angle_type)
    while deg != "":
        quadrant = check_num(float(deg))
        ra = ref_angle(float(deg))  # ra = reference angle
        print(f'\nThe reference angle is:  {Back.LIGHTMAGENTA_EX}{Fore.BLACK}{ra}\u00b0'
              f'{Back.RESET}{Fore.RESET}\n')
        print(f'{Back.BLACK}{float(deg):,}\u00b0{Back.RESET} is positioned in the'
              f' {Style.BRIGHT}{Fore.CYAN}\033[1m{quadrant}{Style.RESET_ALL} quadrant.')  # \u00b0 is degree symbol;
        # \033[1m should be bold, not sure if working
        print("\n----------------------------------\n\n")
        deg = input("Enter the degree: ")


if __name__ == "__main__":
    main()
    # angle_type = input("What is your angle mode? (Radians/Degrees)\n>>> ")
    # deg = input("Enter your degree: ")
    # print(convert_angle(x=float(deg), a_type=angle_type))
