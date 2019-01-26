"""
这个东西比较复杂，没搞懂，待深入了解
将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
"""

s = "print('helloworld')"

r = compile(s, "<string>", "exec")

exec(r)
