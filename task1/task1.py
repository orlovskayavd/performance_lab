import sys

if len(sys.argv) < 2:
    print("Error: No arguments provided. Usage: python task1.py <n> <m>")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Error: Only one argument provided. Usage: python task1.py <n> <m>")
    sys.exit(2)

try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except ValueError:
    print("Enter integers!")
    exit(3)
    
if n <= 0 or m <= 0:
    print ("The numbers must be greater than 0!")
    exit(4)
    
current_n = 0
result = []

while True:
    result.append(current_n + 1)
    current_n = (current_n + m - 1) % n
    if current_n == 0:
        break
    
output = ''.join(map(str, result))

if len(output) > 100:
    print(output[:100] + "...")
else:
    print(output)