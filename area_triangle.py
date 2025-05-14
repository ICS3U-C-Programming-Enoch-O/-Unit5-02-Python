#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 22, 2025
# The calculate_area() function calculates the area of a triangle

import math


def calculate_area(base: int, height: int) -> None:

    # Calculating the area
    area = 0.5 * base * height

    # output
    print(f"The area is {area:.2f} cm²")


def main() -> None:
    # The main() function just calls other functions, returns None.

    # input
    base = input("Enter the base of a triangle (cm): ")
    height = input("Enter the height of a triangle (cm): ")
    print("")
    try:
        base_int = int(base)
        height_int = int(height)
        calculate_area(base, height)
    except Exception:
        print("This is not a valid integer")

    print("\nDone.")


if __name__ == "__main__":
    main()
