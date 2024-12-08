import json


values_file = "values.json"
tests_file = "tests.json"
report_file = "report.json"

try:
    with open(values_file, 'r')as vf:
        values_data = json.load(vf)
        if not isinstance(values_data, dict) or "values" not in values_data:
            raise ValueError("Invalid format in values.json. Expected key 'values'.")
        values_data = values_data["values"]
        
    with open(tests_file, 'r')as tf:
        tests_data = json.load(tf)
        if not isinstance(tests_data, dict) or "tests" not in tests_data:
            raise ValueError("Invalid format in tests.json. Expected key 'tests'.")
        
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    exit(2)
except ValueError as e:
    print(f"Error in file structure: {e}")
    exit(3)
        
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
    exit(4)