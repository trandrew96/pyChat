from .Command import Command
import datetime

class BroadcastCommand(Command):

  def __init__(self, user, msg, sb):
    super().__init__(user, msg, sb)

  def get_timestamp(self):
    now = datetime.datetime.now()

    h = str(now.hour)
    m = str(now.minute)
    s = str(now.second)

    if len(h) < 2:
      h = "0" + h
    if len(m) < 2:
      m = "0" + m
    if len(s) < 2:
      s = "0" + s

    return h+":"+m+":"+s

  def execute(self):
    room = self.user.room

    
    new_msg = "[{0}][{1}]: {2}".format(self.get_timestamp(), self.user.alias, self.msg)

    if room:
      print('{0} is trying to broadcast to {1}'.format(self.user.alias, self.user.room.name))
      room.update(self.user, new_msg)
    else:
      self.sb.update_landing(self.user, new_msg)