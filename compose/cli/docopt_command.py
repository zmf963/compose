from __future__ import absolute_import
from __future__ import unicode_literals

from inspect import getdoc

from docopt import docopt
from docopt import DocoptExit

# 获取一个docopt对象
def docopt_full_help(docstring, *args, **kwargs):
    try:
        return docopt(docstring, *args, **kwargs)
    except DocoptExit:
        raise SystemExit(docstring)

# 参数的处理
class DocoptDispatcher(object):

    def __init__(self, command_class, options):
        self.command_class = command_class
        self.options = options

    def parse(self, argv):
        """参数处理
        """
        command_help = getdoc(self.command_class)  # 获取帮助文档
        options = docopt_full_help(command_help, argv, **self.options)
        command = options['COMMAND']

        if command is None:
            raise SystemExit(command_help)

        handler = get_handler(self.command_class, command)
        docstring = getdoc(handler)

        if docstring is None:
            raise NoSuchCommand(command, self)

        command_options = docopt_full_help(docstring, options['ARGS'], options_first=True)
        return options, handler, command_options

# 获取command_class类中的command方法
def get_handler(command_class, command):
    command = command.replace('-', '_')
    # 我们当然希望有"exec"命令，因为Docker客户机就是这样的。
    # 但在python中，exec是一个关键字
    if command == "exec":
        command = "exec_command"

    if not hasattr(command_class, command):
        raise NoSuchCommand(command, command_class)

    return getattr(command_class, command)

# 定义一个异常，没有这个命令
class NoSuchCommand(Exception):
    def __init__(self, command, supercommand):
        super(NoSuchCommand, self).__init__("No such command: %s" % command)

        self.command = command
        self.supercommand = supercommand
