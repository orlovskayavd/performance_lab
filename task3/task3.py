import sys
import json
import os


if len(sys.argv) < 2:
    print("Error: No arguments provided. Usage: python task3.py <values.json> <tests.json> <report.json>")
    sys.exit(1)
if len(sys.argv) < 4:
    print("Error: Incorrect number of arguments provided. Usage: python task3.py <values.json> <tests.json> <report.json>")
    sys.exit(2)
    
values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]


if values_file == tests_file or values_file == report_file or report_file == tests_file:
    print("Error: Input files must be different from the output file!")
    sys.exit(3)

if os.path.exists(report_file):
    with open(report_file, 'r') as rf:
        if len(rf.read().strip()) > 0:
            print(f"Error: {report_file} already contains data. Please use a new or empty report file.")
            sys.exit(4)

try:
    with open(values_file, 'r') as vf:
        values_data = json.load(vf)
        if not isinstance(values_data, dict) or "values" not in values_data:
            raise ValueError("Invalid format in values.json. Expected key 'values'.")
        values_data = values_data["values"]
        
    with open(tests_file, 'r') as tf:
        tests_data = json.load(tf)
        if not isinstance(tests_data, dict) or "tests" not in tests_data:
            raise ValueError("Invalid format in tests.json. Expected key 'tests'.")
        
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(5)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    sys.exit(6)
except ValueError as e:
    print(f"Error in file structure: {e}")
    sys.exit(7)


values_dict = {item["id"]: item["value"] for item in values_data}

def fill_values(node, values):
    node_id = node.get("id")
    if node_id in values:
        node["value"] = values[node_id]
    else:
        node["value"] = None
        
    if "values" in node:
        for child in node["values"]:
            fill_values(child, values)

for test in tests_data["tests"]:
    fill_values(test, values_dict)

try:
    with open(report_file, 'w') as rf:
        json.dump(tests_data, rf, indent=4)
        print(f"Report successfully saved to {report_file}")
except IOError as e:
    print(f"Error saving report: {e}")
    sys.exit(8)