# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# 创建文本然后写入内容
with open("./data.txt", "w", encoding="utf-8") as f:
    # ./是本项目地址，w 是覆盖写入，可以换成 a--附加写入，可以换成 r+ --读写
    f.write("hello\n")
    # \n是换行符
    f.write("yoooo")

with open("./data2.txt", "a", encoding="utf-8") as f:
    f.write("hello\n")
    f.write("world\n")
    f.write("测试\n")

print('hello word')
print('hello kitty')

money = 9.9
print(money, type(money))