from .Command import Command

class ErrorCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print("{0} entered an invalid command: {1}".format(self.user.get_alias(), self.msg))

    new_msg = "server: you entered an invalid command '{0}'".format(self.msg)

    self.user.update(new_msg)