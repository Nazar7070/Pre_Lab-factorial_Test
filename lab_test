import math

def grade_scale(score):
    """Перетворює оцінку (0-100) у відповідний університетський рівень."""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return 'Invalid score'

    grades = {
        (90, 100): 'A',
        (80, 89): 'B',
        (70, 79): 'C',
        (60, 69): 'D',
        (50, 59): 'E',
        (30, 49): 'FX',
        (0, 29): 'F'
    }

    for (low, high), grade in grades.items():
        if low <= score <= high:
            return grade

    return 'Invalid score'


def factorial(n):
    """Обчислює факторіал числа n."""
    if not isinstance(n, int) or n < 0:
        return 'Invalid input'
    return math.prod(range(1, n + 1)) if n > 0 else 1


def main():
    try:
        score = float(input("Введіть оцінку (0-100): "))
        grade = grade_scale(score)
        print(f"Ваша оцінка: {grade}")
    except ValueError:
        print("Будь ласка, введіть коректну оцінку!")

if __name__ == "__main__":
    main()
