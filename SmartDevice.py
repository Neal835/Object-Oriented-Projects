class SmartDevice:
    def __init__(self,name, is_on=False):
        self.name=name
        self.is_on=is_on
    def toggle_power(self):
        if self.is_on==False:
            self.is_on=True
            print(self.is_on)
        else:
            self.is_on=False
            print(self.is_on)
    def get_status(self):
        if self.is_on== False:
            return("The SmartDevice is off") 
        else:
            return("The SmartDevice is on")
class Light(SmartDevice):
    def __init__(self,name,is_on=False,brightness_level=0):
        super().__init__(name,is_on)
        self.brightness_level=brightness_level 
    def set_brightness(self,level):
        if 100>=level>=0:
            self.brightness_level=level
            return(self.brightness_level)
        else:
            return("That is outside the range of this life")
    def get_status(self):
        if  self.is_on==False:
            return("The Light is off")
        else:
            return("The light is on and has a brightness level of "+str(self.brightness_level)+" ")
class Thermostat(SmartDevice):
    def __init__(self,name,current_temperature, target_temperature,is_on=False):
        super().__init__(name,is_on)
        self.current_temperature=current_temperature
        self.target_temperature=target_temperature
    def set_target_temperature(self,temp):
        self.target_temperature=temp
    def adjust_temperature(self):
        self.current_temperature=self.target_temperature    
    def get_status(self):
        if self.is_on==False:
            return("The Thermostat is off")
        else:
            return("The Thermostat is on and the current_temperature is "+str(self.current_temperature)+". The target temperature is set to "+str(self.target_temperature)+"  ")            
class DoorLock(SmartDevice):
    def __init__(self,name,is_locked,is_on=False):
        super().__init__(name,is_on)
        self.is_locked=is_locked
    def lock(self):
        if self.is_locked==False:
            self.is_locked=True
    def unlock(self):
        if self.is_locked==True:
            self.is_locked==False       
    def get_status(self):
        if is_on==False:
            return("The smart DoorLock is off") 
        elif is_locked==False :
            return("The smart DoorLock is on and is not locked ")
        else:
            return("The smart DoorLock is on and locked")
class Smart_Home:
    def __init__(self):
        self.devices=[]                                    
    def add_device(self,device):
        self.devices.append(device)
    def controll_device(self,device_name, action, *args):
        device_object=None
        for i in range(len(self.devices)):
            if self.devices[i].name==device_name:
                device_object=self.devices[i]
        if callable(getattr(device_object,action)):
            method=getattr(device_object,action)
            method(*args)
    def report_all_statuses(self):
        for i in range(len(self.devices)):
            print(self.devices[i].get_status())
home=Smart_Home()
light=Light("light",False,0)
thermostat=Thermostat("thermostat", False, 34,89)  
home.add_device(light)
home.add_device(thermostat)
light.toggle_power()
print(light.set_brightness(50))
thermostat.set_target_temperature(56)
light.toggle_power()
home.report_all_statuses()
home.controll_device("light","set_brightness",23)
