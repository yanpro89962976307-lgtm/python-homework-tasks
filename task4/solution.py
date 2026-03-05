import sys

def main():
    if len(sys.argv) < 2:
        return

    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            nums = [int(line.strip()) for line in f if line.strip()]
        
        if not nums:
            return

        nums.sort()
        median = nums[(len(nums) - 1) // 2]
        
        total_moves = sum(abs(num - median) for num in nums)
        
        if total_moves <= 20:
            print(total_moves)
        else:
            print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
            
    except Exception:
        pass

if __name__ == "__main__":
    main()
