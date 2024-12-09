n, m = map(int, input("Enter n and m separated by a space: ").split())

try:
    if n <= 0 or m <= 0:
        print ("The numbers must be greater than 0!")
        exit()
except ValueError:
    print("Enter integers!")
    exit()
    
########
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