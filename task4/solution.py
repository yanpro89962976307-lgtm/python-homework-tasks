import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, 'r', encoding='utf-8') as f:
            nums = [int(line.strip()) for line in f if line.strip()]

        if not nums:
            sys.exit(1)

        nums.sort()
        median = nums[len(nums) // 2]

        moves = sum(abs(x - median) for x in nums)

        if moves <= 20:
            print(moves)
        else:
            print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
