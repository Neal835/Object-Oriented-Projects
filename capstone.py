class Location:
    def __init__(self,name,points,type):
        self.name=name
        self.type=type
        self.points=points
         
        
    def does_point_exist(self,point):
        if point in self.points:
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
        self.positions={}
        self.length=length
        self.width=width
        self.locations=[]
        self.type=type
    def add_location(self,l):
        self.locations.append(l)
    def add_position(self):
        for i in range(self.width):
            for j in range(self.length):
                for k in range(len(self.locations)):
                    if self.locations[k].does_point_exist((i,j))==True:
                        #if  len(self.locations[k].points)==1:
                        self.positions[(i,j)]=" X " 
                    elif (i,j) not in self.positions :
                        self.positions[(i,j)]=" * "
# make dictionary for self.positions
    def draw_map(self):
        for i in range(self.width):
            print("")
            for j in range(self.length):
                    print(self.positions[(i,j)],end="")

map=Map(3,4)
tree=Location("tree",[(0,0),"obstacle")
stairs=Location("stairs",[(2,1)],"obstacle")
map.add_location(tree)
map.add_location(stairs)
map.add_position()
map.draw_map()

     
