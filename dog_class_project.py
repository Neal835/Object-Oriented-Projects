class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says woof!"

my_dog = Dog("Buddy")
print my_dog.bark()

class Pet:
  def __init__(self,animal,age,name):
    self.animal=animal
    self.age=age
    self.name=name
  def speak(self):
    if self.animal=="cat":
      return self.name + " says meow."
    elif self.animal=="dog":
      return self.name + " says woof."
    elif self.animal=="cow":
      return self.name + " says moo."
    else:
      return self.name + " says aargh"
  def birthday(self):
    self.age+=1
    return ""+self.name+"'s new age is "+str(self.age)+" "
pet=Pet("cat",3,"Fluffy")    
print pet.speak()
print pet.birthday()
pettwo=Pet("cow",8,"Bessie")
print pettwo.speak()
print pettwo.birthday()
