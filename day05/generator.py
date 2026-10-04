def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

print(list(read_large_file("generator.py")))