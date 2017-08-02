from .Command import Command
import socket

class SetAliasCommand(Command):
  def __init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print("{0} wants to set their alias to {1}".format(self.user.get_alias(), self.msg))

    msg_elements = self.msg.split()

    if (len(msg_elements) == 1) and (self.sb.set_alias(self.user, msg_elements[0])):
      self.user.update("201 {0}".format(self.msg))
    else:
      self.user.update("\nAlias is either taken or invalid")