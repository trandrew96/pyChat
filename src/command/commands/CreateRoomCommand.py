from .Command import Command

class CreateRoomCommand(Command):

  def __init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print('{0} is creating a room with name \'{1}\''.format(self.user.get_alias(), self.msg))

    msg_elements = self.msg.split(' ')

    if len(msg_elements) != 1:
      self.user.update('\nserver: invalid use of /create_room command')
    elif self.user.room:
      self.user.update('\nserver: you must leave your current room before creating one')
    else:
      if self.sb.create_room(self.user, self.msg):
        self.user.update('\nserver: welcome to your room')
      else:
        self.user.update('\nserver: a room with that name already exists')