"""特殊方法跟普通方法"""


class Calculator:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"calculator with current value:{self.value}"

    def add(self, amount):
        self.value += amount
        return self.value


cal = Calculator(8)
num = cal.add(6)


# 特殊方法__str__会在尝试打印对象时被自动调用
print(cal)
print(num)
