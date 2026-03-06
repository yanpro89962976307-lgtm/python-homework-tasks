import sys

def get_path(n, m):
    if n == 1:
        return "1"
    
    path = []
    current = 1  
    while True:
        path.append(str(current))
        current = (current + m - 2) % n + 1
        
        if current == 1:
            break
    return "".join(path)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    parts = list(map(int, input_data))
    result = ""
    
    
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            n = parts[i]
            m = parts[i+1]
            result += get_path(n, m)
    
    print(result)

if __name__ == "__main__":
    main(
