import turtle
turtle1=turtle.Turtle()
class Shape:
    def __init__(self, color,shape, num_sides,size):
        self.color = color
        self.shape = shape
        self.num_sides =num_sides
        self.size=size

    def draw(self):
        return "Drawing a  "+self.size+"  "+ self.color + " "+self.shape+". "
    def draw_shape(self):
      turtle1.color(self.color)
      if self.size=="small":
        for i in range(int(self.num_sides)):
          turtle1.forward(400/int(self.num_sides))
          turtle1.left(360/int(self.num_sides))
      
      if self.size=="medium":
        for i in range(int(self.num_sides)):
          turtle1.forward(450/int(self.num_sides))
          turtle1.left(360/int(self.num_sides))
      
      if self.size=="large":
        for i in range(int(self.num_sides)):
          turtle1.forward(600/int(self.num_sides))
          turtle1.left(360/int(self.num_sides))    
class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)
while 1==1:
  my_canvas = Canvas()
  breakq=input("Would you like to stop making more shapes?")
  if breakq=="Yes":
    break
  else:
    colorq=input("What color would you like your shape to be? ")
    sizeq=input("What size would you like your shape to be? ")
    shapeq=input("What shape would you like?" )
    sideq=input("How many sides does your shape have? " )
    my_shape = Shape(colorq,shapeq,sideq,sizeq)
    my_canvas.add_shape(my_shape)
    print my_canvas.shapes[0].draw()
    my_canvas.shapes[0].draw_shape()
