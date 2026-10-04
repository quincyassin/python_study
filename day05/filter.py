scores = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 55},
]

passed = filter(lambda s: s["score"] >= 60, scores)

print(passed)           # <filter object at 0x10xxxxx>
print(len(passed))      # ❌ TypeError: object of type 'filter' has no len()
print(list(passed))     # ✅ [{'name': '张三', 'score': 85}]
print(list(passed))     # ❌ []  —— 空了！只能遍历一次