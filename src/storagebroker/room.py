class Room(object):

  def __init__(self, user, name):
    self.admin = user
    self.name = name

    #users: (alias, user)
    self.users = {}
    self.users[user.alias] = user
    
    #blocked: list of blocked users
    self.blocked = []
    self.log = []

  def register(self, user):

    print('trying to register {0} with room {1}'.format(user.alias, self.name))
    
    if user not in self.blocked:

      self.users[user.alias] = user
      user.room = self

      if len(self.log) > 0:

        log_msg = '\nserver: welcome to {0}. here is what you missed...'.format(self.name)

        log_msg += '\n━━━━━━━━━━━━━━━━━━\n{0} CHAT LOG\n──────────────────'.format(self.name)        
        for msg in self.log:
          log_msg += '\n' + msg
        log_msg += '\n━━━━━━━━━━━━━━━━━━\n'

        user.update(log_msg)

      else:
        user.update('\nserver: welcome to {0}'.format(self.name))

      self.update(user, 'server: {0} has joined {1}'.format(user.alias, self.name))

      return True

    else:

      user.update('\nserver: permission denied. you are blocked from {0}'.format(self.name))
      return False

  def detach(self, user):
    print('removing user from room "{0}"'.format(self.name))

    if user in self.users.values():
      del self.users[user.alias]
      user.room = None
      print('{0} has been detached from {1}'.format(user.alias, self.name))
      self.update(user, 'server: {0} has left {1}'.format(user.alias, self.name))


  def update(self, sender, msg):
    for user in self.users.values():
      if user != sender:
        user.update(msg)

    if not msg.startswith('server'):
      if len(self.log) < 20:
        self.log.append(msg)
      else:
        self.log.pop(0)
        self.log.append(msg)

  def population(self):
    return len(self.users)

  def getUsers(self):
    return self.users.values()

  def block(self, user):
    self.blocked.append(user)
    self.admin.update('server: you blocked {0} from joining {1}'.format(user.alias, self.name))
    self.detach(user)
    user.update('server: you have been blocked from {0}. taking you to the landing'.format(self.name))
    
  def unblock(self, user):
    if user in self.blocked:
      self.blocked.remove(user)
      self.update(self.admin, 'server: {0} has been unblocked from {1}'.format(user.alias, self.name))
      self.admin.update('server: you unblocked {0} from {1}'.format(user.alias, self.name))
      user.update('server: you have been unblocked from {0}'.format(self.name))