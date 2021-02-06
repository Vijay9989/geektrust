from src.family.representative import Representative
from src.family.constants import Gender, Constants

class Clan(object):
  def __init__(self):
    self.clanHead = None
	
  def addClanHead(self, name, gender):
    self.clanHead = Representative(name, gender)
	
  def addSpouse(self, representativeName, spouseName, gender):
    representative = self.__searchRepresentative(self.clanHead, representativeName)
    if representative != None and representative.spouse == None:
      spouse = Representative(spouseName, gender)
      spouse.addSpouse(representative)
      representative.addSpouse(spouse)
  
  def addchild(self, motherName, childName, gender):
    representative = self.__searchRepresentative(self.clanHead, motherName)
    if representative == None:
      result = Constants.PERSON_NOT_FOUND.value
    elif childName == None or gender == None:
      result = Constants.CHILD_ADDITION_FAILED.value
    elif representative.gender == Gender.Female.name:
      child = Representative(childName, gender, representative, representative.spouse)
      representative.addChild(child)
      result = Constants.CHILD_ADDITION_SUCCEEDED.value
    else:
      result = Constants.CHILD_ADDITION_FAILED.value
    return result 
  
  def __searchInLaws(self, representative, gender):
    personName = representative.name
    if representative.spouse != None and representative.spouse.mother != None:
      result = representative.spouse.mother.searchChild(gender)
      if representative.spouse.name in result:
        result.remove(representative.spouse.name)
    elif representative.mother != None:
      result = representative.mother.searchSiblingRelation(gender, representative.name)
    if not result:
      return None
    else:
      return ' '.join(result)
  
  def __searchRepresentative(self, head, representativeName):
    if representativeName == None or head == None:
      return None
    representative = None
    if representativeName == head.name:
      return head
    elif head.spouse != None and representativeName == head.spouse.name:
      return head.spouse
    childlist = []
    if head.gender == Gender.Female.name:
      childlist = head.children
    elif head.spouse != None:
      childlist = head.spouse.children
    for child in childlist:
      representative = self.__searchRepresentative(child, representativeName)
      if representative != None:
        break
    return representative
  
  def getRepresentatives(self, person, relationship):
    representative = self.__searchRepresentative(self.clanHead, person)
    if representative == None:
      return Constants.PERSON_NOT_FOUND.value
    elif relationship == None:
      return Constants.PROVIDE_VALID_RELATION.value
    else:
      return self.getRelationship(representative, relationship)
  
  def getRelationship(self, representative, relationship):
    relationships = {
      'Daughter' : lambda : ' '.join(representative.searchChild(Gender.Female.name)),
      'Son' : lambda : ' '.join(representative.searchChild(Gender.Male.name)),
      'Siblings' : lambda : representative.searchSiblings(),
      'Sister-In-Law' : lambda : self.__searchInLaws(representative, Gender.Female.name),
      'Brother-In-Law' : lambda : self.__searchInLaws(representative, Gender.Male.name),
      'Maternal-Aunt' : lambda : representative.mother.searchAuntOrUncle(Gender.Female.name),
      'Paternal-Aunt' : lambda : representative.father.searchAuntOrUncle(Gender.Female.name),
      'Maternal-Uncle' : lambda : representative.mother.searchAuntOrUncle(Gender.Male.name),
      'Paternal-Uncle' : lambda : representative.father.searchAuntOrUncle(Gender.Male.name)
    }
    if relationship not in relationships:
      return constants.NOT_YET_IMPLEMENTED.value
    if relationship == ('Maternal-Aunt' or 'Maternal-Uncle') and representative.mother == None:
      return None
    if relationship == ('Paternal-Aunt' or 'Paternal-Uncle') and representative.father == None:
      return None
    else:
      return relationships.get(relationship, lambda: 'Invalid')()