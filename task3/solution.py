import json
import sys

def fill_values(tests, values_map):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_map:
            test['value'] = values_map[test_id]
        if 'values' in test:
            fill_values(test['values'], values_map)

def main():
    if len(sys.argv) < 4:
        return

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    try:
        with open(values_path, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        
        values_map = {item['id']: item['value'] for item in values_data.get('values', [])}

        with open(tests_path, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)

        if 'tests' in tests_data:
            fill_values(tests_data['tests'], values_map)

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(tests_data, f, indent=2, ensure_ascii=False)

    except Exception:
        pass

if __name__ == "__main__":
    main(
