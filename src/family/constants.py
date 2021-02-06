from enum import Enum

class Constants(Enum):
  NOT_YET_IMPLEMENTED = 'NOT YET IMPLEMENTED'
  PERSON_NOT_FOUND = 'PERSON_NOT_FOUND'
  PROVIDE_VALID_RELATION = 'PROVIDE VALID RELATION'
  CHILD_ADDITION_FAILED = 'CHILD_ADDITION_FAILED'
  CHILD_ADDITION_SUCCEEDED = 'CHILD_ADDITION_SUCCEEDED'
  INVALID_COMMAND = 'INVALID COMMAND!'
  NONE = 'NONE'

class Gender(Enum):
  Male = 0
  Female = 1