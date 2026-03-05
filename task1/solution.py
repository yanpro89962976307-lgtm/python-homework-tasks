import sys

def get_circular_path(n, m):
    if n == 0:
        return ""
    res = []
    current = 0
    while True:
        res.append(str(current + 1))
        current = (current + m - 1) % n
        if current == 0:
            break
    return "".join(res)

def main():
    if len(sys.argv) < 2:
        return
    
    args = sys.argv[1:]
    output = []
    
    for i in range(0, len(args), 2):
        if i + 1 < len(args):
            n = int(args[i])
            m = int(args[i+1])
            output.append(get_circular_path(n, m))
            
    print("".join(output))

if __name__ == "__main__":
    main()
