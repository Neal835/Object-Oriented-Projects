class Shape:
    def __init__(self,name):
        self.name=name
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area()")
        return(0)
    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement calculate_perimeter()")
        return(0)        
class Rectangle(Shape):
    def __init__(self,name,width,length):
        super().__init__(name)
        self.width=width
        self.length=length
    def calculate_area(self):
        return(self.width*self.length)
    def calculate_perimeter(self):
        return((2*self.width)+(2*self.length))
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
    def calculate_area(self):
        return(3.1415*self.radius*self.radius)
    def calculate_perimeter(self):
        return((self.radius*2*3.1415))
class Triangle(Shape):
    def __init__(self,name,base_side,height,other_side1,other_side2):
        super().__init__(name)
        self.base_side=base_side
        self.height=height
        self.other_side1=other_side1
        self.other_side2=other_side2
    def calculate_area(self):
        return(self.base_side*self.height*0.5)
    def calculate_perimeter(self):
        return(self.other_side1+self.other_side2+self.base_side)
class Shape_Collection:
    def __init__(self):
        self.shapes=[]
    def add_shape(self,shape):
        self.shapes.append(shape)
    def total_area(self):
        t=0
        for i in range(len(self.shapes)):
            t+=self.shapes[i].calculate_area()
        return(t) 
    def total_perimeter(self):
        t=0
        for i in range(len(self.shapes)):
            t+=self.shapes[i].calculate_perimeter()
        return(t)        
        
square=Rectangle("square",4,4)            
print(square.calculate_area())
print(square.calculate_perimeter())
circle=Circle("circle",5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
triangle=Triangle("triangle",8,6,10,6)
print(triangle.calculate_area())
print(triangle.calculate_perimeter())
shapes=Shape_Collection()
shapes.add_shape(square)
shapes.add_shape(triangle)
shapes.add_shape(circle)
print(shapes.total_area())
print(shapes.total_perimeter())
               
        
