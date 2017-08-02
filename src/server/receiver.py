from ..command.CommandCreator import CommandCreator
import importlib
import queue
import select
import socket
import threading
import sys

'''
CommandReceiver contains the server socket and is the first point of entry
for client input. Responsibilities include:
  - accepting new connections
  - receiving client input, getting appropriate command objects, and 
    enqueing those command objects  onto the command queue
  - removing closed sockets from the database
'''
class CommandReceiver(object):

  def __init__(self, commandQ, sb):
    
    host = 'localhost'
    port = 2080
    self.addr = (host, port)

    self.commandQ = commandQ
    self.sb = sb

    self.servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.servsock.bind(self.addr)
    self.servsock.listen(20)

    #descriptors contains 'waitable objects' (sockets in our case)
    self.descriptors = [self.servsock]

  def run(self):

    while True:
      (sread, swrite, sexc) = select.select(self.descriptors, [], [])

      for sock in sread:
        if sock == self.servsock:

          if len(self.descriptors) < 1000:
            self.accept_new_connection()

        else:
          msg = sock.recv(1024).decode()

          #client closed their connection
          if msg == '':
            self.sb.remove_user(self.sb.get_user(sock))
            self.descriptors.remove(sock)
            sock.close()

          #enque new command
          elif len(msg) != 1:
            user = self.sb.get_user(sock)
            new_command = CommandCreator.get_command(user, msg, self.sb)
            self.commandQ.put(new_command)

  def accept_new_connection(self):
    clisock, (remhost, remport) = self.servsock.accept()
    self.descriptors.append(clisock)
    self.sb.add_connection(clisock)