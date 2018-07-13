```

argparse是python用于解析命令行参数和选项的标准模块，argparse模块的作用是用于解析命令行参数，

例如python  parseTest.py  input.txt  output.txt   --user=name   --port=8080。

二、使用步骤：

1：import argparse

2：parser = argparse.ArgumentParser()

3：parser.add_argument()

4：parser.parse_args()

解释：首先导入该模块；然后创建一个解析对象；然后向该对象中添加你要关注的命令行参数和选项，每一个add_argument方法对应一个你要关注的参数或选项；最后调用parse_args()方法进行解析；解析成功之后即可使用，下面简单说明一下步骤2和3。

 

三、方法ArgumentParser(prog=None, usage=None,description=None, epilog=None, parents=[],formatter_class=argparse.HelpFormatter, prefix_chars='-',fromfile_prefix_chars=None, argument_default=None,conflict_handler='error', add_help=True)

这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，会打印这些描述信息，一般只需要传递description参数，如上。

四、方法add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

其中：

name or flags：命令行参数名或者选项，如上面的address或者-p,--port.其中命令行参数如果没给定，且没有设置defualt，则出错。但是如果是选项的话，则设置为None

nargs：命令行参数的个数，一般使用通配符表示，其中，'?'表示只用一个，'*'表示0到多个，'+'表示至少一个

default：默认值

type：参数的类型，默认是字符串string类型，还有float、int等类型

help：和ArgumentParser方法中的参数作用相似，出现的场合也一致



```
