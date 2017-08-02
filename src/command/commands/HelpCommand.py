from .Command import Command

class HelpCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print("{0} needs our help".format(self.user.get_alias()))

    f = open('src/command/commands/help.txt', 'r')
    contents = '\n' + f.read()
    f.close()

    self.user.update(contents)