import sys

def main():
    if len(sys.argv) < 3:
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        with open(file1, 'r') as f:
            lines = f.readlines()
            x0, y0 = map(float, lines[0].split())
            a, b = map(float, lines[1].split())

        with open(file2, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                px, py = map(float, line.split())
                
                res = ((px - x0)**2 / a**2) + ((py - y0)**2 / b**2)

                if abs(res - 1.0) < 1e-12:
                    print(0)
                elif res < 1.0:
                    print(1)
                else:
                    print(2)
    except Exception:
        pass

if __name__ == "__main__":
    main(
