import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"总耗时:{end_time - start_time:.4f} 秒")
        return result
    return wrapper

def read_scores(file_path: str):
    with open(file_path) as file:
        next(file)
        for line in file:
            line = line.strip()
            if line:
                name, score = line.split(",")
                yield {"name": name, "score": score}

def parse_scores(iterable):
    for item in iterable:
        try:
            item["score"] = float(item["score"])
            yield item
        except ValueError:
            print(f"⚠️ 跳过脏数据: {item['name']} - {item['score']}")

def sort_scores(scores: list):
    return sorted(scores, key=lambda score: score["score"], reverse=True)

def filter_passed(scores: list):
    return filter(lambda score: score["score"] >= 60, scores)

class Scorer:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        print("开始统计")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"统计完成, 共处理 {self.count} 条有效数据")
        return True