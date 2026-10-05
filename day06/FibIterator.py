class FibIterator:
    def __init__(self, n):
        # 存 n，初始化 a、b、计数器
        self.n = n
        self.a = 0
        self.b = 1
        self.current = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        # 1. 检查计数器到 n 没，到了就 raise StopIteration
        # 2. 没到，要做三件事：
        #    - 把 self.a 先存起来（因为要返回它）
        #    - 更新 a, b = b, a + b
        #    - 计数器 +1
        #    - return 存起来的那个值
        if self.current >= self.n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return self.a

for num in FibIterator(10):
    print(num)   # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55