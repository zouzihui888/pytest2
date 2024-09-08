import random
random.seed(0)  # 随机数种子，用于评测，请不要修改


# 在注释语句后面补充合适的代码，使程序能完成预期的功能
def calculator(n, maximum):
    """随机产生n道正整数四则运算的题目,用户输入计算结果，
    判断输入正确与否,并统计正确率。题目保证减法不出现负数."""
    correct = 0
    for i in range(n):  # 循环n次，每次产生一个新问题
        b = random.randint(0, maximum)  # 随机产生一个maximum以内整数
        a = random.randint(b, maximum)  # 随机产生一个b到maximum以内整数，避免减法出现负数
        sign = random.choice('+-*/')    # 随机获取一个运算符号
        # 先输出一个格式化的计算表达式并保持光标不换到下一行，类似5+10=
        print(f'{a}{sign}{b}=', end='')
        # 接受用户输入的一个浮点数，并转换为浮点类型
        user_input = float(input())
        # 如果计算结果正确，输出'恭喜你，回答正确'并统计答对的次数，注意满足条件时执行的语句要缩进
        if sign == '+':
            result = a + b
        elif sign == '-':
            result = a - b
        elif sign == '*':
            result = a * b
        else: # sign == '/'
            result = a / b

        if user_input == result:
            print('恭喜你，回答正确')
            correct += 1
        else:
            print('回答错误，你要加油哦！')        
        # 否则输出'回答错误，你要加油哦！'