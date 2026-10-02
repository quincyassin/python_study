def add_student(name, scores: dict):
    average = sum(scores.values()) / len(scores)
    return {"name": name, "scores": scores, "average": average}

def print_report(student):
    print("===== 成绩单 =====")
    print(f"姓名: {student['name']}")
    for subject, score in student['scores'].items():
        print(f"{subject}: {score}")
    print(f"平均分: {student['average']:.2f}")
    if student['average'] >= 90:
        print("等级: A")
    elif student['average'] >= 80:
        print("等级: B")
    elif student['average'] >= 60:
        print("等级: C")
    else:
        print("等级: D")
    print("=" * 17)

scores1 = { "语文" : 85 , "数学" : 92 , "英语" : 78 }
student1 = add_student( "小明" , scores1)
print_report(student1)

import random

def guess_number():
    num = random.randint(1, 100)
    print("请猜一个1到100之间的数字")
    count = 0
    while True:
        guess = int(input("猜一个 1~100 的数字："))
        count += 1
        if guess == num:
            print("恭喜你猜对了")
            print(f"你猜了 {count} 次")
            break
        elif guess > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")
    return count
guess_number()