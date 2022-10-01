'九九乘法表 2022-09-21'
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={i*j:<2}", end="  ")
    print()
