def simple_iterator(data):
    index = 0
    while index < len(data):
        yield data[index]
        index += 1


def count_up_to(n):
    for i in range(1, n + 1):
        yield i


def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":
    print(list(simple_iterator([10, 20, 30])))
    print(list(count_up_to(5)))
    print(list(even_numbers(10)))
    print(list(fibonacci(7)))