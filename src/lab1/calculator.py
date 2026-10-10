"""Модуль простого калькулятора."""


def add(a: float, b: float) -> float:
    """Сложить два числа."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычесть из первого числа второе."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножить два числа."""
    return a * b


def divide(a: float, b: float) -> float:
    """Разделить первое число на второе."""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b


def main() -> None:
    """Запустить программу и запросить данные у пользователя."""
    print("Выберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа!")
        return

    if choice == "1":
        print(f"Результат: {add(num1, num2)}")
    elif choice == "2":
        print(f"Результат: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Результат: {multiply(num1, num2)}")
    elif choice == "4":
        try:
            print(f"Результат: {divide(num1, num2)}")
        except ValueError as error:
            print(f"Ошибка: {error}")
    else:
        print("Неверный выбор операции.")


if __name__ == "__main__":
    main()
