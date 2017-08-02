from .commands.SetAliasCommand import SetAliasCommand
from .commands.BroadcastCommand import BroadcastCommand
from .commands.HelpCommand import HelpCommand
from .commands.CreateRoomCommand import CreateRoomCommand
from .commands.DisplayUsersCommand import DisplayUsersCommand
from .commands.JoinRoomCommand import JoinRoomCommand
from .commands.LeaveRoomCommand import LeaveRoomCommand
from .commands.UnblockCommand import UnblockCommand
from .commands.ErrorCommand import ErrorCommand
from .commands.BlockCommand import BlockCommand
from .commands.DeleteCommand import DeleteCommand
from .commands.DisplayRoomsCommand import DisplayRoomsCommand
from .commands.SetAdminCommand import SetAdminCommand
import re

#CommandCreator is a creator/factory class that creates command objects
class CommandCreator(object):

  comm_dict = {}
  comm_dict["set_alias"] = SetAliasCommand
  comm_dict["broadcast"] = BroadcastCommand
  comm_dict["help"] = HelpCommand
  comm_dict["create"] = CreateRoomCommand
  comm_dict["create_room"] = CreateRoomCommand
  #globals()["display_users"] = DisplayUsersCommand
  comm_dict["join_room"] = JoinRoomCommand
  comm_dict["join"] = JoinRoomCommand
  comm_dict["leave"] = LeaveRoomCommand
  comm_dict["unblock"] = UnblockCommand
  comm_dict["block"] = BlockCommand
  comm_dict["delete"] = DeleteCommand
  comm_dict["error"] = ErrorCommand
  comm_dict["display_rooms"] = DisplayRoomsCommand
  comm_dict["rooms"] = DisplayRoomsCommand
  comm_dict["set_admin"] = SetAdminCommand

  '''
  get_command_type extracts the '[command_type]' in the '/[command_type]' part of the string
  '''
  def get_command_type(msg):

    m = re.match('(^/\w*)\1?\s?(.*)\2?', msg)
    return m.group(1).strip("/")

  '''
  trim_msg will remove the '/[command_type]' part of the msg string
  and return the rest of string.
  '''
  def trim_msg(msg):
    m = re.match('(^/\w*)\1?\s?(.*)\2?', msg)

    comm_type = m.group(1)
    new_msg = msg.replace(comm_type, "")
    new_msg = new_msg.lstrip()

    return new_msg

  '''
  get returns a command object of type corresponding to the '/[command_type]'
  part of the msg string. If [command_type] is not a valid command type,
  then it returns an Error command.
  '''
  def get_command(user, msg, sb):

    comm_type = CommandCreator.get_command_type(msg)
    if not comm_type:
      return ErrorCommand(user, msg, sb)

    msg = CommandCreator.trim_msg(msg)

    #if the msg contains a valid command return the appropriate command object
    if comm_type in CommandCreator.comm_dict.keys():
      return CommandCreator.comm_dict[comm_type](user, msg, sb)
    else:
      return ErrorCommand(user, msg, sb)