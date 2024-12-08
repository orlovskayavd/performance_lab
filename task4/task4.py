try:
    input_file = open('input.txt', 'r')
    nums = []
    for line in input_file.readlines():
        nums.append(int(line.strip()))
    input_file.close()
except ValueError:
    print("The file contains incorrect data!")
    exit()
    
if not nums:
    print("The file is empty!")
    exit()

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