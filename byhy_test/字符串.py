'''
题目1
请大家写一行代码，定义一个Python字符串变量 内容为 hello world
题目2
请大家写一行代码，定义一个Python字符串变量 内容为 你好世界
题目3
请大家写一行代码，定义一个Python字符串变量 内容为 他说：'你好'
注意，字符串里面有英文的单引号
再写一行代码，定义一个Python字符串 内容为 他说："你好"
注意，字符串里面有英文的双引号
题目4
请大家写一行代码，定义一个Python字符串变量 内容为
他说：'你
好'
注意，字符串里面有新的一行
题目5
有如下的代码，定义了一个Python字符串
str1 = '大家好，我的名字叫：黑羽白月'
请接下来写一行代码，使用字符串切片的方法 ，打印出 str1里面的人名字。
'''
hello_world = 'hello world'
ni_hao_sigai = '你好世界'
he_say_nihao1 = "他说'你好'"
he_say_nihao2 = '他说"你好"'
he_say_nihao3 = "他说'你\n好'"
str1 = '大家好，我的名字叫：黑羽白月'
print(str1[-4:])
print(he_say_nihao3)
