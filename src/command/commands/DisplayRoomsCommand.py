from .Command import Command

class DisplayRoomsCommand(Command):

  def	__init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def execute(self):
      rooms = self.sb.rooms

      room_str = "\n━━━━━━━━━━━━━━━━━━\nRoom, Population\n──────────────────\nlanding, {0}".format(len(self.sb.landing))

      if rooms:
        for room_name, room_instance in rooms.items():
          room_str += "\n{0}, {1}".format(room_name, room_instance.population())

      room_str += '\n━━━━━━━━━━━━━━━━━━'

      self.user.update(room_str)