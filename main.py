"""Демонстрация работы калькулятора."""

from calculator import add, divide, is_even, multiply, subtract


def main() -> None:
    print("=== Калькулятор ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 4 = {divide(10, 4)}")
    print(f"Число 4 чётное: {is_even(4)}")


if __name__ == "__main__":
    main()
