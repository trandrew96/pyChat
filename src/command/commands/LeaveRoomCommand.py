from .Command import Command

class LeaveRoomCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
    print("{0} wants to leave their room".format(self.user.alias))

    room = self.user.room

    if not room:
      self.user.update("\nerror: you can't leave the landing")

    elif room and room.admin != self.user:
      self.user.update('removing you from {0}'.format(room.name))
      room.detach(self.user)
      self.user.room = None
      self.sb.landing.append(self.user)

    elif room.admin == self.user:
      self.sb.delete_room(self.user.room)