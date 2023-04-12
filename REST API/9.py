#PRODUCE JSON AND DECODE JSON TO STRING
import json


class Vehicle:
    def __init__(self, registration_number, year_of_production, pessanger,mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.pessanger = pessanger
        self.mass = mass

class Encoder(json.JSONEncoder):
    def default(self,v):
        if isinstance(v, Vehicle):
            return v.__dict__
        else:
            return super().default(self,z)


class Decoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.decode_veh)

    def decode_veh(self,d):
        return Vehicle(**d)




vehicle_data = []
veh = Vehicle("PC38927Z", 2018,False, 1543.2)


users_choice = None
while users_choice not in ["1","2"]:
    users_choice = input("What can I do for you?\n\
1 - produce a JSON string describing a vehicle\n\
2 - decode a JSON string into vehicle data\n\
Your choice: ")
if users_choice == '1':
    json_string = json.dumps(veh, cls = Encoder)
    print("Registration number: "+veh.registration_number)
    print("Year of production: "+str(veh.year_of_production))
    print("Passenger [y/n]: "+"y") if veh.pessanger else print("Passenger [y/n]: "+"n")
    print("Vehicle mass: "+str(veh.mass))
    print("Resulting JSON string is:\n",json_string)
    
    print("Done")
else:
    str_to_decode = input("Enter vehicle JSON string: ")
    #print(str_to_decode)
    try:
        json_obj = json.loads(str_to_decode,cls = Decoder)
        dict_json_obj = json_obj.__dict__
        #print(type(json_obj),json_obj)
    except Exception as e:
        print("The input should be in a form of dictionary. The keys are:\nregistration_number,year_of_production,pessanger,mass")
        print(e)
    else:
        if len(list(dict_json_obj.keys()))==4:
            if ["registration_number","year_of_production","pessanger","mass"].sort() != list(dict_json_obj.keys()).sort():
                print("The dict key names are not matching")
            else:
                if isinstance(dict_json_obj["registration_number"], str) and isinstance(dict_json_obj["year_of_production"], int)\
                and isinstance(dict_json_obj["pessanger"], bool) and type(dict_json_obj["mass"]) in (float, int):
                    print(dict_json_obj)
                    vehicle_data.append(json_obj)
                    print("Done")
                else:
                    print("Type of one/multiple attribute/s is incorrect")     
        else:
            print("Number of parameters (keys) should be 4")
                
        

        
