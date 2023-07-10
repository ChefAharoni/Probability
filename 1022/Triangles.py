import math


def solve():
    # import math
    # define a module that takes two data pieces in a triangle and solves the rest.
    # i.e. - get one side and one angle, module solves the rest of the sides ang the angles
    # support for radians, degrees, and degrees minutes seconds (DMS).
    pass


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
        d = x * (180/math.pi)
    elif a_type == "Degrees" or a_type.startswith("Deg"):
        # Convert Degrees to Radians
        d = x * (math.pi/180)
    else:
        raise ValueError
    return d


def main():
    given_angle = input("Please enter the given angle: ")
    given_side = input("Please enter the given side: ")


if __name__ == "__main__":
    main()

