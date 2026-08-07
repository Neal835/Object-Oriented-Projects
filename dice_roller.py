import random
class Dice:
  def __init__(self,sides=6):
    self.sides=sides
    self.history=[]
  def roll(self):
    answer=random.randint(1,self.sides)
    self.history.append(answer)
    return answer
  def average(self):
    sums=0
    for i in range (len(self.history)):
      sums+=self.history[i]
    average=sums/len(self.history)
    return average
  def dicehistory(self):
    return self.history
dice=Dice()
print dice.roll()
print dice.roll()
print dice.roll()
print dice.average()
print dice.dicehistory()
dice_two=Dice(20)
print dice_two.roll()
print dice_two.roll()
print dice_two.roll()
print dice_two.average()
print dice_two.dicehistory()
