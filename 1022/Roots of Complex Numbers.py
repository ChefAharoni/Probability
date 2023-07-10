import AngleQuadrantFinder as AQF
import math
from colorama import Style, Back, Fore


def calc(x: float):
    #r ^ (1/n)[Cos((theta/n))+(K*360/n)) + iSin((theta/n)+(K*360/n))]
    #where k = 0,1,2,3....n-1


def main():
    deg = input("Enter your degree: ")
    ra = AQF.ref_angle(float(deg))
    print(f'\nThe reference angle is:  {Back.LIGHTMAGENTA_EX}{Fore.BLACK}{ra}\u00b0'
          f'{Back.RESET}{Fore.RESET}\n')


if __name__ == "__main__":
    main()
