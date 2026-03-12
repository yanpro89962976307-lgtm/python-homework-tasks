import sys
import json

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test.get("id")
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        
        if "values" in test:
            fill_values(test["values"], values_dict)

def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    v_path, t_path, r_path = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        with open(v_path, 'r', encoding='utf-8') as f:
            v_data = json.load(f)
        with open(t_path, 'r', encoding='utf-8') as f:
            t_data = json.load(f)

        v_dict = {item["id"]: item["value"] for item in v_data.get("values", [])}

        if "tests" in t_data:
            fill_values(t_data["tests"], v_dict)

        with open(r_path, 'w', encoding='utf-8') as f:
            json.dump(t_data, f, indent=2, ensure_ascii=False)

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
