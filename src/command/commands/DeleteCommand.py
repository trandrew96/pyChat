from .Command import Command

class DeleteCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):

    if not self.user.room:
      self.user.update('\nerror: invalid use of /delete command')
    elif self.user.room.admin != self.user:
      self.user.update('\nerror: you are not admin of {0}'.format(self.user.room.name))
    else:
      self.sb.delete_room(self.user.room)