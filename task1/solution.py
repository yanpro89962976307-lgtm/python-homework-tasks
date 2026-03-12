import sys


def get_circular_path(n, m):
    path = []
    current = 1

    while True:
        path.append(str(current))
        current = (current + m - 2) % n + 1

        if current == 1:
            break

    return "".join(path)


def main():
    if len(sys.argv) != 5:
        print("Ошибка: Введите 4 аргумента (n1 m1 n2 m2)")
        sys.exit(1)

    try:
        n1, m1 = int(sys.argv[1]), int(sys.argv[2])
        n2, m2 = int(sys.argv[3]), int(sys.argv[4])

        if n1 <= 0 or m1 <= 0 or n2 <= 0 or m2 <= 0:
            print("Ошибка: Параметры должны быть положительными числами.")
            sys.exit(1)

        res1 = get_circular_path(n1, m1)
        res2 = get_circular_path(n2, m2)

        print(res1 + res2)

    except ValueError:
        print("Ошибка: Все аргументы должны быть целыми числами.")
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

