import socket
import threading
 
class Client(object):

  def __init__(self):
    self.server_addr = ('127.0.0.1', 2080)
    self.remsock = socket.socket()

  def run(self):
    self.register_thread()

  #if no command, append '/broadcast' to the left of the string and return string
  #if command then return string
  def parse_user_input(msg):

    msg = msg.lstrip()

    if msg.startswith('/'):
      return msg
    else:
      return '/broadcast ' + msg

  '''
  register_thread is called for connecting the user to the server,
  and subsequently registering the user with an alias. Once a valid 
  alias is entered the inputstream and outputstream threads will start
  '''
  def register_thread(self):
    
    self.remsock.connect(self.server_addr)

    print("connected to the server ")

    isRegistered = False
    while not isRegistered:
      
      alias = input("enter your alias: ")
      msg = '/set_alias ' + alias
      self.remsock.send(msg.encode())

      inbox = self.remsock.recv(1024).decode()
      if(inbox.startswith("201")):
        isRegistered = True

    self.alias = alias

    print('\nHi {0}, welcome to the landing. Enter \'/help\' to see available commands.\n'.format(alias))

    t_output = threading.Thread(target=self.outputstream)
    t_input = threading.Thread(target=self.inputstream)

    t_output.start()
    t_input.start()

  '''
  outputstream is the thread function for receiving user input and
  sending it to the server
  '''
  def outputstream(self):

    message = input(self.alias + ": ")
    message = Client.parse_user_input(message)
    while message != '/q':
      self.remsock.send(message.encode())
      message = input(self.alias + ": ")
      message = Client.parse_user_input(message)
             
    self.remsock.close()

  '''
  inputstream is the thread function for receiving server output and
  printing it on the screen
  '''
  def inputstream(self):

    while True:

      try:
        data = self.remsock.recv(1024).decode()
      except:
        pass

      if not data:
        break

      if data.startswith("201"):
        self.alias = data.split()[1]
      else:
        print (str(data))

if __name__ == '__main__':
    client = Client()
    client.run()