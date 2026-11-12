class Location:
    def __init__(self,name,positions,type):
        self.positions=positions
        self.name=name
        self.type=type
         
        
    def does_point_exist(self,point):
        if point in self.positions:
            return True
        else:
            return False    

class Students:
    def __init__(self,name,position,speed,orientation,has_disability=False ):
        self.name=name
        self.position=position
        self.speed=speed
        self.orientation
        self.has_disabilty=False
    def change_position(self, new_position):
        self.position=new_position        
class Map:
    def __init__(self,length,width):
        self.length
        self.width
        self.locations=[]
    def add_location(self,l):
        self.locations.append(l)
# make dictionary for self.positions
    def draw_map(self):
        for i in range(self.width):
            for j in range(self.length):
                    for k in range(len(self.locations)):
                        if (i,j) in self.locations[k].positions:
                            print(self.locations[k].positions[(i.j)])
                        else:
                            print("*")    
                            
m=Map()
print(m.add_positions(3,4))


     
