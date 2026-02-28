import math
import random


def basic_operations(a, b):
    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else None
    }


def power_and_root(x):
    return {
        "square": x ** 2,
        "cube": x ** 3,
        "sqrt": math.sqrt(x) if x >= 0 else None
    }


def rounding_examples(x):
    return {
        "round": round(x),
        "floor": math.floor(x),
        "ceil": math.ceil(x)
    }


def trigonometry(angle_deg):
    rad = math.radians(angle_deg)
    return {
        "sin": math.sin(rad),
        "cos": math.cos(rad),
        "tan": math.tan(rad)
    }


def random_examples():
    return {
        "random_float": random.random(),
        "random_int": random.randint(1, 100),
        "random_choice": random.choice(["apple", "banana", "cherry"]),
        "random_sample": random.sample(range(1, 20), 5)
    }


def statistics(values):
    return {
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values)
    }


if __name__ == "__main__":
    print("Basic:", basic_operations(10, 3))
    print("Power:", power_and_root(9))
    print("Rounding:", rounding_examples(3.7))
    print("Trig:", trigonometry(30))
    print("Random:", random_examples())
    print("Stats:", statistics([1, 2, 3, 4, 5]))