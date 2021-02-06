from src.family.constants import Gender, Constants
import src.family.exceptions as my_exec
import os

class ProcessFileHandler(object):
  def processFile(self, clan, file, isInitFile):
    if os.path.exists(file):
      with open(file) as f:
        lines = [line.rstrip() for line in f]
      num_lines = sum(1 for line in open(file))
      if lines:     
        if isInitFile:
          self.processInitFile(clan, lines, num_lines)
        else:
          self.processInputFile(clan, lines, num_lines)
      else:
        raise my_exec.FileException('Can\'t read file at absolute location "{}" because it\'s empty'.format(file))
    else:
      raise my_exec.FileException('Can\'t open file at absolute location "{}" because it\'s not found'.format(file))

  def processInitFile(self, clan, lines, num_lines):
    for i in range(num_lines):
      commandParams = lines[i].split(';')
      if commandParams[0] == 'ADD_FAMILY_HEAD':      
        clan.addClanHead(commandParams[1],commandParams[2])
      elif commandParams[0] == 'ADD_CHILD':
        clan.addchild(commandParams[1], commandParams[2], commandParams[3])
      elif commandParams[0] == 'ADD_SPOUSE':
        clan.addSpouse(commandParams[1],commandParams[2],commandParams[3])
      else:
        print(Constants.INVALID_COMMAND.value)

  def processInputFile(self, clan, lines, num_lines):
    for i in range(num_lines):
      commandParams = lines[i].split(' ')
      if commandParams[0] == 'ADD_CHILD':
        print(clan.addchild(commandParams[1], commandParams[2], commandParams[3]))      

      elif commandParams[0] == 'GET_RELATIONSHIP':
        print(clan.getRepresentatives(commandParams[1], commandParams[2]))
      else:
        print(Constants.INVALID_COMMAND.value)