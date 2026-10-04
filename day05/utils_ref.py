"""
参考版本：学生成绩统计系统 - 工具模块
包含：生成器、装饰器、上下文管理器、异常处理
"""
import time
import functools


# ========== 装饰器 ==========

def timer(func):
    """计时装饰器：打印函数执行耗时"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱️  {func.__name__} 耗时: {elapsed:.4f}秒")
        return result
    return wrapper


def log(level="DEBUG"):
    """带参数的日志装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 调用了 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ========== 生成器 ==========

def read_scores(filepath):
    """生成器：逐行读取 CSV，跳过表头，yield 字典"""
    with open(filepath) as f:
        next(f)   # 跳过表头（也可以用 for 循环计数）
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, score = line.split(",")
            yield {"name": name, "score": score}


def parse_scores(iterable):
    """生成器：把 score 转成 float，跳过脏数据"""
    for item in iterable:
        try:
            item["score"] = float(item["score"])
            yield item
        except ValueError:
            print(f"⚠️  跳过脏数据: {item['name']} - {item['score']}")


# ========== 上下文管理器 ==========

class Scorer:
    """成绩统计上下文管理器：用 with 自动打印开始/结束"""
    def __init__(self):
        self.count = 0

    def __enter__(self):
        print("=== 开始统计 ===")
        return self   # 返回 self，可以在 with 里用 as 接收

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"=== 统计完成，共处理 {self.count} 条有效数据 ===")
        # 返回 True 表示异常已处理，不再往外抛
        return True


# ========== 工具函数 ==========

def sort_scores(scores):
    """按分数降序排序"""
    return sorted(scores, key=lambda s: s["score"], reverse=True)


def filter_passed(scores):
    """过滤出及格（≥60）的学生"""
    return filter(lambda s: s["score"] >= 60, scores)
