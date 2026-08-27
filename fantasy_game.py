class Character:
  def __init__(self,name,health,original_health,status):
    self.name=name
    self.health=health
    self.original_health=original_health
    self.status=status
  def take_damage(self,amount):
    if self.health>0:
      self.health-=amount
      if self.health>0:
        return(" "+self.name+" has lost "+str(amount)+" health ")
      else:
        return(" "+self.name+" has died")
    else:
      return("The dead can not take more damage")
      self.status="Dead"
  def attack(self,target):
    print(target.take_damage(100))
    return(" "+self.name+" has attacked "+target.name+" ")
class Warrior(Character):
  def attack(self,target):
    print(target.take_damage(150))
    return(" "+self.name+" has used high meele damage to hurt "+target.name+" ")
  def heal(self):
    healthq=input("How much would you like to heal by? You can not get more than what you started. ")
    if healthq<= self.original_health-self.health:
      self.health+=int(healthq)
class Mage(Character):
  def attack(self,target):
    print(target.take_damage(110))
    return(" "+self.name+" has used magic damage to hurt "+target.name+" ")
  def fireball(self, characters_list):
    for i in range (len(characters_list)):
      print(characters_list[i].take_damage(175))
    return("The mage used fireball")  
class Rogue(Character):
  def __init__(self,name,health,original_health,stealth,status):
    super().__init__(name,health,original_health,status)
    self.stealth=stealth
  def attack(self,target):
    print(target.take_damage(125))
    self.stealth+=1
    return(" "+self.name+" has used moderate stealth damage to hurt "+target.name+" ")
  def stealth_attack(self,target):
    if self.stealth>10:
      print(target.take_damage(200))
      return(" "+self.name+" has used large stealth damage to hurt "+target.name+" ")
    else:
      return("You need to attack more characters in order to use this ability")
    
class Character_List:
  def __init__(self):
    self.character_list=[]
  def add(self, character ):
    self.character_list.append(character)
cl=Character_List()
mage=Mage("John",300,300,"Alive")
cl.add(mage)
warrior=Warrior("Gandalf",300,300,"Alive")
cl.add(warrior)
rogue=Rogue("Koga",300,300,"Alive",0)
cl.add(mage)
goblin=Character("Goblin",300,300,"Alive")
cl.add(goblin)
print(goblin.attack(mage))
print(mage.fireball(cl.character_list))

    
