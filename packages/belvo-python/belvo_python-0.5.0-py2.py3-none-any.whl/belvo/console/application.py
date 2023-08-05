from cleo import Application

from .commands.about import AboutCommand
from .commands.shell import ShellCommand

application = Application()
application.add(AboutCommand())
application.add(ShellCommand())
