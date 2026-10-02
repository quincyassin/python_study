book = {
    "title": "Python 从入门到实践",
    "author": "Eric Matthes",
    "pages": 320,
    "price": 39.99
}
print(book["title"])
print(book.get("title"))
print(book.get("ISBN", "未知"))
book["price"] = book["price"] * 0.8
book["tags"] = ["编程", "技术"]
for k, v in book.items():
    print(f"{k}: {v}")

student = ("小明", 20, 95.5)
name, age, score = student
print(f"{name}, {age}岁, 分数 {score}")
student[0] = "小红"
a = 10
b = 20
a, b = b, a