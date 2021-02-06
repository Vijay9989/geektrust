from src.family.processFileHandler import ProcessFileHandler
from src.family.clan import Clan
import pathlib
import os
import sys

def main():
  clan = Clan()

  file_name = 'input/initInput.txt'
  dir = pathlib.Path().absolute()
  
  fileProcessor = ProcessFileHandler()

  fullPath = os.path.join(dir, file_name)
  fileProcessor.processFile(clan, fullPath, True)

  fullPath = os.path.join(dir, sys.argv[1])
  fileProcessor.processFile(clan, fullPath, False)

if __name__ == '__main__':
  main()