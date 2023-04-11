class Tires:
    def __init__(self,size):
        self.size=size
        self.pumped=0
        
    def get_pressure(self):
        if self.pumped==0:
            print("No pressure, needs to pump.")
        else:
            print("Pumped. High pressure")
        
    def pump(self):
        print("Pumping the tyres")
        self.pumped=1

class Engine:
    def __init__(self,fuel):
        print(fuel)
        self.fuel=fuel
        self.count=0
    
    def start(self):
        if self.count==1:
            print("Engine is on")
        else:
            print("Starting the {} car".format(self.fuel))
            self.count=1
        
    
    def stop(self):
        if self.count==0:
            print("Engine is off")
        else:
            print("Stopping the {} car".format(self.fuel))
            self.count=0
    
    def get_state(self):
        if self.count==0:
            print("Car is off.")
        else:
            print("Car is on.")
    

class Vehicle:
    def __init__(self,VIN,engine,tires):
        self.VIN=VIN
        self.engine=engine
        self.tires=tires
    
    
    
class CityTires(Tires):
    def __init__(self):
        super().__init__(15)
        print("City Tires: 15 size")
class OffroadTires(Tires):
    def __init__(self):
        super().__init__(18)
        print("Off-road Tires: 18 size")
        
class Electric(Engine):
    def __init__(self):
        super().__init__("Electric")
        
class Petrol(Engine):
    def __init__(self):
        super().__init__("Petrol")
    
    
city_car=Vehicle("1234",Electric(),CityTires())
city_car.engine.start()
city_car.tires.get_pressure()
city_car.tires.pump()
city_car.tires.get_pressure()

print('-------')

all_terrain=Vehicle("4444",Petrol(),OffroadTires())
all_terrain.engine.start()
all_terrain.tires.get_pressure()
all_terrain.tires.pump()
all_terrain.tires.get_pressure()
all_terrain.engine.get_state()


    
    
    

