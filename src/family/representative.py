from src.family.constants import Gender, Constants

class Representative(object):
  def __init__(self, name, gender, mother=None, father=None):
    self.name = name
    self.gender = gender
    self.mother = mother
    self.father = father
    self.spouse = None             
    self.children = []
 
  def addChild(self, child):
    self.children.append(child)
 
  def addSpouse(self, spouse):
    self.spouse = spouse
 
  def searchChild(self, gender):
    result = []
    for child in self.children:
      if child.gender == gender:
        result.append(child.name)
    if not result: 
      return Constants.NONE.value
    else:
      return result
 
  def searchSiblings(self):
    result = []
    if self.mother != None:
      for child in self.mother.children:
        if not self.name == child.name:
            result.append(child.name)
    if not result: 
      return Constants.NONE.value
    else:
      return ' '.join(result)

  def searchSiblingRelation(self, gender, personName):
    result = []
    for child in self.children:
      if child.spouse != None and not personName == child.name:
        if child.spouse.gender == gender:
          result.append(child.spouse.name)
    if not result: 
      return Constants.NONE.value
    else:
      return ' '.join(result)

  def searchAuntOrUncle(self, gender):
    result = []
    if self.mother != None:
      for child in self.mother.children:
        if not self.name == child.name and child.gender == gender:
          result.append(child.name)
    if not result: 
      return Constants.NONE.value
    else:
      return ' '.join(result)