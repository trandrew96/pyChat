from .Command import Command

class DisplayUsersCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
      print("{0} wants to see the users in room {1}".format(self.user.alias, self.msg))

      user_dict = self.user.room.users
      listOfUsers = "server: "
      for alias in user_dict:
          listOfUsers = listOfUsers + alias + ", "
      listOfUsers = listOfUsers[:-2]
      self.user.update(listOfUsers) 
