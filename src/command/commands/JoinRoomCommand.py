from .Command import Command

class JoinRoomCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):

    msg_elements = self.msg.split()
    
    if len(msg_elements) != 1:
      self.user.update('\nserver: invalid use of /join_room command')
    else:
      self.sb.join_room(self.user, self.msg)