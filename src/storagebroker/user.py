class User(object):

  def __init__(self, remsock, alias):
    self.clisock = remsock
    self.alias = alias
    self.room = None

  def change_alias(self, new_alias):
    self.alias = new_alias

  def get_alias(self):
    return self.alias

  def update(self, msg):
    self.clisock.send(msg.encode('utf-8'))

  def set_room(self, room):
    self.room = room