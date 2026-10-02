print("=== 学生成绩管理系统 ===")


students = [
    { "name" : "小明" , "score" : 60 },
    { "name" : "小红" , "score" : 90 },
    { "name" : "小刚" , "score" : 70 },
    { "name" : "小美" , "score" : 80 }
]
while True:
    student_len = len(students)
    print("\n")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 计算平均分")
    print("4. 查看前三名")
    print("5. 退出")
    num = int(input("请选择操作（1-5）:"))
    
    if num == 1:
        name = input("请输入学生姓名:")
        score = float(input("请输入学生成绩:"))
        student_dict = {"name": name, "score": score}
        students.append(student_dict)
        print("添加成功")
    elif num == 2:
        print("所有学生信息:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']}, {student['score']}")
    elif num == 3:
        sum_scores = 0
        for student in students:
            sum_scores += student["score"]
        avg_score = sum_scores / student_len
        print(f"平均分: {avg_score:.2f}")
    elif num == 4:
        if student_len < 3:
            print("学生数量不足，无法查看前三名")
        else:
            students_sopy = sorted(students, key=lambda s: s["score"], reverse=True)
            # students_sopy = students[:]
            # for i in range(student_len - 1):
            #     for j in range(i + 1, student_len):
            #         if students_sopy[i]["score"] < students_sopy[j]["score"]:
            #             students_sopy[i], students_sopy[j] = students_sopy[j], students_sopy[i]
            for i in range(3):
                print(f"{i + 1}.{students_sopy[i]['name']}: {students_sopy[i]['score']}分")
    elif num == 5:
        print("退出")
        break