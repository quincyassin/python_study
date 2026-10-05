class ScoreCollector:
    def __init__(self):
        self.scores = []        # 存成绩列表
        self.index = 0          # 迭代器用的索引

    # —— 上下文管理器 ——
    def __enter__(self):
        print("开始收集成绩")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"收集完成，共 {len(self.scores)} 条")
        return True

    # —— 迭代器协议 ——
    def __iter__(self):
        self.index = 0          # ⚠️ 每次迭代要重置索引！
        return self

    def __next__(self):
        if self.index >= len(self.scores):
            raise StopIteration
        score = self.scores[self.index]
        self.index += 1
        return score

    # —— 业务方法 ——
    def add(self, name, score):
        self.scores.append({"name": name, "score": score})


with ScoreCollector() as sc:
    sc.add("张三", 90)
    sc.add("李四", 75)
    sc.add("王五", 88)
    
    for item in sc:          # 同一个对象既能 with 又能 for！
        print(item)

    print ( "=== 第二次迭代（同一个 sc）===" ) 
    for item in sc: # 再迭代一次，应该还能跑！ 
        print (item)