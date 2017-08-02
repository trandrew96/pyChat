import socket

class Command(object):

  def __init__(self, user, msg, sb):
    self.user = user
    self.msg = msg
    self.sb = sb

  def execute(self):
    pass