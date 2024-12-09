import sys


if len(sys.argv) < 2:
    print("Error: No arguments provided. Usage: python task4.py <input.txt>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found!")
    sys.exit(2)
except ValueError:
    print("The file contains incorrect data!")
    sys.exit(3)
    
if not nums:
    print("The file is empty!")
    sys.exit(4)

nums = sorted(nums)

n = len(nums)
if n  % 2 == 1:
    median = nums[n // 2]
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) // 2

min_step = 0
for num in nums:
    min_step += abs(num-median)
    
print(min_step)