from .Command import Command

class BlockCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    self.sb.block_user(self.user, self.msg)