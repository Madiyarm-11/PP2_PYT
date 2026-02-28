import json


def parse_json(json_string):
    return json.loads(json_string)


def create_json(data):
    return json.dumps(data)


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def read_json_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def update_json_value(data, key, value):
    data[key] = value
    return data


if __name__ == "__main__":
    raw = '{"name":"Alice","age":25,"skills":["Python","SQL"],"active":true}'
    parsed = parse_json(raw)
    print(parsed)

    parsed = update_json_value(parsed, "age", 26)
    print(create_json(parsed))

    print(pretty_json(parsed))