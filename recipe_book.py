class Recipe:
  def __init__(self, name,cooking_time,ingredients):
    self.name=name
    self.cooking_time=cooking_time
    self.ingredients=ingredients
  def __str__(self):
     return("The dish is called "+self.name+", it has a cook time of "+str(self.cooking_time)+", and contains "+str(self.ingredients))
class Recipe_Book:
  def __init__(self):
    self.recipes=[]
  def add(self,recipe):
    self.recipes.append(recipe)
  def find(self,name):
    for i in range(len(self.recipes)):
      if self.recipes[i].name==name:
        return(str(self.recipes[i]))
  def total_cook_time(self):
    time=0
    for i in range(len(self.recipes)):
      time+=self.recipes[i].cooking_time
    return(time)
  def find_ingredient(self, ingredient):
    recipes_with_ingredient=[]
    for i in range(len(self.recipes)):
      if ingredient in self.recipes[i].ingredients:
        recipes_with_ingredient.append(self.recipes[i].name)
    return(recipes_with_ingredient)
  def remove(self,name):
    for i in range(len(self.recipes)):
      if self.recipes[i].name==name:
        self.recipes.pop(i)
  def find_recipes(self):
    recipesf=[]
    while 1==1:
      ingredientsq=input("What ingredients do you have? When you are done entering items, say Stop")
      if ingredientsq != "Stop":
        recipesf.append(str(ingredientsq))
      else:
        break
    precipes=[]  
    for i in range(len(self.recipes)):
      all_ingredients=True
      for j in range(len(self.recipes[i].ingredients)):
        if self.recipes[i].ingredients[j] not in recipesf:
          all_ingredients=False
      if all_ingredients ==True:
        precipes.append(self.recipes[i].name)
    if len(precipes)>0:
      return(precipes)
    else:
      return("You can not make any of recipes in the book.")
        
          
          
        
      
pasta=Recipe("pasta",5, ["eggs","flour"])
print(pasta)
rb=Recipe_Book()
rb.add(pasta)
print(rb.total_cook_time())
