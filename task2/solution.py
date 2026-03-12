import sys

def main():
    if len(sys.argv) != 3:
        print("Ошибка: нужно указать 2 файла")
        sys.exit(1)

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(ellipse_file) as f:
        cx, cy = map(float, f.readline().split())
        rx, ry = map(float, f.readline().split())

    with open(points_file) as f:
        for line in f:
            x, y = map(float, line.split())

            value = ((x - cx) ** 2) / (rx ** 2) + ((y - cy) ** 2) / (ry ** 2)

            if abs(value - 1) < 1e-9:
                print(0)
            elif value < 1:
                print(1)
            else:
                print(2)

if __name__ == "__main__":
    main()
