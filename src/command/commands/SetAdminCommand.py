from .Command import Command

class SetAdminCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print('{0} wants to give admin privileges to {1}'.format(self.user.alias, self.msg))

    if not self.user.room:
      self.user.update('\nerror: the landing does not support admin privileges')
    elif self.user.room.admin != self.user:
      self.user.update('\nerror: you are not admin of {0}'.format(self.user.room.name))
    elif self.msg not in self.user.room.users.keys():
      self.user.update('\nerror: {0} is not in {1}'.format(self.msg, self.user.room.name))
    else:
      self.user.room.admin = self.user.room.users[self.msg]
      self.user.update('\nserver: you gave your admin privileges to {0}'.format(self.msg))
      self.user.room.users[self.msg].update('server: {0} has made you admin of {1}'.format(self.user.alias, self.user.room.name))
