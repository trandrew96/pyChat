from .receiver import CommandReceiver
from .invoker import CommandInvoker
from ..storagebroker.StorageBroker import StorageBroker
import queue
import threading

'''
Server simply contains the objects that make the program run.
This class doesn't do any actual work.
'''
class Server(object):

  def __init__(self):

    self.commandQ = queue.Queue(100)
    self.sb = StorageBroker()

    self.receiver = CommandReceiver(self.commandQ, self.sb)
    self.invoker = CommandInvoker(self.commandQ, self.sb)

  def run(self):

    t_receiver = threading.Thread(target=self.receiver.run)
    t_invoker = threading.Thread(target=self.invoker.run)

    t_receiver.start()
    t_invoker.start()

if __name__ == '__main__':
    s = Server()
    s.run()