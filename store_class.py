
class Store_Item:
  def __init__(self,name,original_price,price,discount):
    self.name=name
    self.original_price=original_price
    self.price=price
    self.discount=discount
    self.discounts=[]
  def apply_discount(self):
    self.price=self.price-((self.discount/100)*self.price)
    self.discounts.append(self.discount)
    return("%0.2f"%self.price)
  def get_price(self):
    print("The current price of "+self.name+" is $"+str(self.price)+" ")
  def reset_price(self):
    self.price=self.original_price
  def set_discount(self,new_value):
    self.discount=new_value
  def discounts_applied(self):
    return(self.discounts)
notebook=Store_Item("Notebook",3,3,25)
print notebook.apply_discount()
notebook.get_price() 
notebook.reset_price()
notebook.get_price()
notebook.set_discount(10)
print notebook.apply_discount()
print notebook.discounts_applied()
