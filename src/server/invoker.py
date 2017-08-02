import queue
import threading

'''
CommandInvoker simply pops new commands off the command queue
and executes them
'''
class CommandInvoker(object):
  def __init__(self, commandQ, sb):
    self.commandQ = commandQ
    self.sb = sb

  def run(self):
    while True:
      com = self.commandQ.get()
      com.execute()