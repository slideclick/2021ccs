# -*- coding: UTF-8 -*- cp936
'''
python编辑器基本要求(Geany能满足)--尽量少移动光标,少移动到鼠标
以下按照优先级排序
1.C:\WINDOWS\SHELLNEW下面做个模板文件
2. 设置tab为空格:检验办法就是按完tab按backspace看回到哪里的光标.npp在language里面
3.使用shift tab反缩进.或者tab需要光标在行首,最好的是ctrl[](evevnote是ctrl M)
4.在:后回车自动缩进.如果在缩进块里面多按一个回车,能够自动回到行首就好了.
不过好像有时为了可读就是不能那样 例如一个try下面分几部分都是一个缩进
5.选中几行代码之后按Tab全部进，按Shift+Tab全部后退一个。
6.支持立即运行从编辑器中,例如ctrl B
或者你使用ipython的 %run 命令,然后你手工调用函数
'''
import sys
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # python -m unittest discover
    # python -m pip install django
    try:
        print("hello你好")
    except KeyboardInterrupt:
        print ("interruptted by Ctrl-c")
    sys.exit(1)