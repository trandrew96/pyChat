from .Command import Command

class UnblockCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print("{0} wants to unblock {1}".format(self.user.get_alias(),self.msg))
    
    if not self.user.room:
      self.user.update('\nserver: you can\'t unblock people in the landing')
    elif self.user.room.admin != self.user:
      self.user.update('\nserver: non-admin users can\'t unblock')
    else:
      for person in self.sb.users.values():
        if person.alias == self.msg:
          blockee = person
          self.user.room.unblock(blockee)
          return

      self.user.update('\nserver: no user with alias {0}'.format(self.msg))