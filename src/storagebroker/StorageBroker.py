from .user import User
from .room import Room

'''
This class handles our main data (User, Room, and socket objects).
'''
class StorageBroker(object):

  def __init__(self):
    #users dict: (socket, User)
    self.users = {}

    #rooms (key, value) = (room_name, room)
    self.rooms = {}

    #list of users with no room
    self.landing = []

    self.taken_alias = []

  '''
  add_connection is called whenever the receiver accepts a new socket.
  Each socket has a corresponding User instance, with it's temporary
  alias set to anon#, where # = current number of users
  '''
  def add_connection(self, clisock):
    print('adding new connection {0}'.format(clisock.getpeername()))

    temp_alias = "anon" + str(len(self.users))
    self.taken_alias.append(temp_alias)

    user = User(clisock, temp_alias)

    self.users[clisock] = user
    self.landing.append(user)

  def get_user(self, clisock):
    return self.users[clisock]

  '''
  set_alias changes the alias of the user if alias is available.
  must update the alias
  '''
  def set_alias(self, user, alias):
    if len(alias) < 50 and alias not in self.taken_alias:
      self.taken_alias.remove(user.alias)
      self.taken_alias.append(alias)

      if user.room:
        user.room.users[alias] = user.room.users.pop(user.alias) 

      user.alias = alias

      return True
    else:
      user.update('\nthat name is already taken')
      return False

  '''
  create_room makes a room instance with room_name = name and
  admin = user. Returns True if room_name is available
  '''
  def create_room(self, user, name):
    if name not in self.rooms:
      room = Room(user, name)
      user.room = room
      self.rooms[name] = room
      self.landing.remove(user)
      return True
    else:
      return False

  '''
  join_room adds the user to the room corresponding with roomname.
  Removes user from landing. Returns True if successful.
  '''
  def join_room(self, user, roomname):
    if roomname in self.rooms:
      if self.rooms[roomname].register(user):
        user.room = self.rooms[roomname]
        self.landing.remove(user)
        return True
      else:
        return False
    else:
      user.update('\nserver: {0} does not exist.'.format(roomname))
      return False

  '''
  leave_room removes the user from their room.
  Returns False if unsuccessful (user is in the landing).
  '''
  def leave_room(self, user):
    room = user.room

    if room.admin == user:
      self.delete_room(room)
    elif user not in user.room.users.values():
      return False
    else:
      self.landing.append(user)
      user.room.detach(user)
      user.room = None
      return True

  def update_landing(self, user, msg):
    for u in self.landing:
      if u != user:
        u.update(msg)

  def delete_room(self, room):
    room.update(room.admin, '\nserver: {0} is now closing. moving to landing'.format(room.name))
    room.admin.update('\nserver: {0} is now closing. moving to landing'.format(room.name))

    print('deleting {0}'.format(room.name))

    for u in room.users.values():
      self.landing.append(u)
      u.room = None

    del self.rooms[room.name]

  def block_user(self, user, msg):
    if user in self.landing or msg not in user.room.users:
      user.update('\nerror: invalid use of block. enter \'/help\' to learn more about commands')
    elif user.room.admin != user:
      user.update('\nerror: only admin can block users')
    elif user == user.room.users[msg]:
      user.update('\nerror: you can\'t block yourself')
    else:
      blockee = user.room.users[msg]
      user.room.block(blockee)
      self.landing.append(blockee)
      blockee.room = None

  #remove user when they log out or unexpectedly close the program
  def remove_user(self, user):
    if user.room:
      user.room.detach(user)
    else:
      self.landing.remove(user)

    print('{0} logged out'.format(user.alias))

    self.taken_alias.remove(user.alias)

    del self.users[user.clisock]

  def displayUsers(self, sock):
    user = self.users[sock]

    if user.room:
      return user.room.getUsers()