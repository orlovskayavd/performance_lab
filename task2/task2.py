import math
import sys


if len(sys.argv) < 2:
    print("Error: No arguments provided. Usage: python task2.py <circle_file> <points_file>")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Error: Only one file provided. Usage: python task2.py <circle_file> <points_file>")
    sys.exit(2)

circle_file = sys.argv[1]
points_file = sys.argv[2]

try:
    with open(circle_file, 'r') as file:
        x_c, y_c = map(float, file.readline().split())
        r = float(file.readline().strip())

    with open(points_file, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
    
    results = []
    for x, y in points:
        d = math.sqrt((x - x_c) ** 2 + (y - y_c) ** 2)
        if d == r:
            results.append(0)
        elif d < r:
            results.append(1)
        else:
            results.append(2)
        
    for res in results:
        print(res)
    
except FileNotFoundError as e:
    print(f"Error:{e}")
    sys.exit(3)
except ValueError:
    print("Error: Incorrect data format in one of the files.")
    sys.exit(4)