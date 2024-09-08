def solve(a,b):  # 这是函数的定义，先不用理解，程序会执行缩进块的代码
    # 在下面输入你的代码，计算a和b的和、差和积并分三行输出
    print(a + b)
    print(a - b)
    print(a * b)
    

if __name__ == '__main__':
    a = int(input())  # 输入转为整数
    b = int(input())  # 输入转为整数
    solve(a,b)        # 调用定义的函数solve(a,b)，执行函数中的代码
