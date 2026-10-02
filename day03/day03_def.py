def calculate_bmi(height, weight):
    print(f"BMI={weight/ (height * height)}")

calculate_bmi(175, 150)

def calculate_bmi(height, weight):
    return weight/ (height * height)
result = calculate_bmi(1.75, 75)
print(f"BMI={result}")


def create_user(username, age, is_vip=False):
    return {"username": username, "age": age, "is_vip": is_vip}
user = create_user("ricardo", 25)
vip_user = create_user("ricardo", 25, True)
print(user)
print(vip_user)

x = 10 
def foo ():
    x = 20 
    print ( f"函数里的 x: {x} " )

foo() 
print ( f"函数外的 x: {x} " )