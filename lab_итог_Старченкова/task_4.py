import json

INPUT_FILE = "output.csv"

def csv_to_list_dict(INPUT_FILE, sign=',') -> list[dict]:
    head_list = []
    rows_list = []
    with open(INPUT_FILE, 'r') as f:
        head_lines = f.readlines()
        head_lines_ = head_lines[0].rstrip().split(sign)
        for head in head_lines[1:]:
            rows_list.append(head.rstrip().split(sign))
        for row in rows_list:
            i = {k: v for k, v in zip(head_lines_, row)}
            head_list.append(i)
    return head_list
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))