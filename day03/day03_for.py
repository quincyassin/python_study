for i in range(2, 11, 2):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1

def countdown(n):
    while n > 0:
        print(n)
        n-=1
    print("发射")
countdown(5)
