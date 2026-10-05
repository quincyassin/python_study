class MyRange:

    def __init__(self, start, end=None):
        # 支持两种调用方式：
        #   MyRange(5)     → start=0, end=5
        #   MyRange(2, 8)  → start=2, end=8
        if end is None:
            end, start = start, 0
        self.end = end
        self.current = start - 1   # 统一公式：先减 1，__next__ 里再加回来

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.end:
            raise StopIteration
        return self.current

# 测试
print("MyRange(1, 5):")
for num in MyRange(1, 5):
    print(num)

print("MyRange(5):")
for num in MyRange(5):
    print(num)

print("MyRange(10, 15):")
for num in MyRange(10, 15):
    print(num)