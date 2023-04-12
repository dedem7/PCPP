#SERVER APPLICATION TO WORK WITH JSON: CRUD

import requests
import json

reply = ""
car_ids = []
def check_server(cid=None):
    global reply
    try:
        if cid:
            reply = requests.get("http://localhost:3000/cars/" + str(cid), timeout=3)
        else:
            reply = requests.get("http://localhost:3000/cars", timeout=3)
    except requests.InvalidURL:
        print("URL or ID is invalid")
        return False
    except requests.RequestException:
        print("No connection")
        return False
    else:
        return True

def print_menu():
    print("+-----------------------------------+",
      "|       Vintage Cars Database       |",
      "+-----------------------------------+",
      "M E N U",
      "=======",
      "1. List cars",
      "2. Add new car",
      "3. Delete car",
      "4. Update car",
      "0. Exit", sep="\n")
    


def read_user_choice():
    user_choice = input("Enter your choice (0..4): ")
    while user_choice not in ["0","1","2","3","4"]:
        user_choice = input("Enter your choice (0..4): ")
    return user_choice
        

def print_header():
    key_names = ["id", "brand", "model", "production_year", "convertible"]
    key_widths = [10, 15, 10, 20, 15]
    for n,w in zip(key_names,key_widths):
        print(n.ljust(w), end="|")
    print()
    print("-"*75)


def print_car(car):
    global car_ids
    key_names = ["id", "brand", "model", "production_year", "convertible"]
    key_widths = [10, 15, 10, 20, 15]
    for k,w in zip(key_names,key_widths):
        if k == "id":
            car_ids.append(car[k])    
        print(str(car[k]).ljust(w), end="|")
    print()
    
        

def update_car_ids():
    global car_ids
    if type(reply.json()) is list and len(reply.json())>0:
        for each in reply.json():
            car_ids.append(each["id"])
    if type(reply.json()) is dict and len(list(reply.json()))>0:
        car_ids.append(reply.json()["id"])
    car_ids = list(set(car_ids))
    
    

def list_cars():
    if type(reply.json()) is list and len(reply.json())>0:
        print_header()
        for car in reply.json():
            print_car(car)
    elif type(reply.json()) is dict and len(list(reply.json()))>0:
        print_header()
        print_car(reply.json())
    else:
        print("*** Database is empty ***")


def name_is_valid(name):
    if name and name.replace(" ","").isalnum():
        return True
    else:
        return False


def enter_id():
    car_id = input("Car ID (empty string to exit): ")
    car_id = car_id.replace(" ","")
    
    if car_id == "" or not car_id.isdigit():
        print("ID should be integer!Try again.")
        return None
    if car_id.isdigit():
        return int(car_id)

def enter_production_year():
    prod_year = input("Car production year, range: 1900 - 2000 (empty string to exit): ")
    prod_year = prod_year.replace(" ","")
    if prod_year == "" or not prod_year.isdigit():
        print("Prod. year should be integer!Try again.")
        return None
    if prod_year.isdigit():
        if 1900 <= int(prod_year) <= 2000:
            return int(prod_year)
        else:
            print("Prod. year should be between 1900 and 2000!Try again.")
            return None


def enter_name(what):
    if what in ('brand','model'):
        brand_model = input("Car " + what + "(empty string to exit): ")
        if name_is_valid(brand_model):
            return str(brand_model)
        if brand_model.replace(" ","") =="":
            print("Brand/Model can't be empty!Try again.")
            return None

def enter_convertible():
    conv = input("Is this car convertible? [y/n] (empty string to exit): ")
    if conv.replace(" ","") == "":
        print("Can't be empty!Try again.")
        return None
    if conv.lower() == "y":
        return True
    if conv.lower() == "n":
        return False


headers = {"Connection":"Close"}
json_type = {"Content-Type":"application/json"}

def delete_car():
    id_to_del = enter_id()
    if id_to_del is None:
        return None
    update_car_ids()
    if check_server(id_to_del):
        del_reply = requests.delete("http://localhost:3000/cars/" + str(id_to_del))
        if del_reply.status_code == requests.codes.ok:
            print("Deleted!")
            car_ids.remove(id_to_del)
        elif del_reply.status_code == requests.codes.not_found:
            print("Not found")
        else:
            print("Can't delete the item")



def input_car_data(with_id):
    if with_id:
        car_id = enter_id()
        if car_id is None: return None
        if car_id in car_ids:
            print("Car with the same ID already exists.")
            return None
        car_brand = enter_name('brand')
        if car_brand is None: return None
        car_model = enter_name('model')
        if car_model is None: return None
        car_year = enter_production_year()
        if car_year is None: return None
        conv = enter_convertible()
        if conv is None: return None
        if [isinstance(car_id,int),isinstance(car_brand,str),isinstance(car_year,int),isinstance(conv,bool)].count(True) == 4:
            return {"id": car_id, "brand": car_brand, "model": car_model, "production_year": car_year, "convertible": conv}
        else:
            print("Check the type of parameters:\n","{'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }")
            return None
    else:
        car_brand = enter_name('brand')
        if car_brand is None: return None
        car_model = enter_name('model')
        if car_model is None: return None
        car_year = enter_production_year()
        if car_year is None: return None
        conv = enter_convertible()
        if conv is None: return None
        if [isinstance(car_brand,str),isinstance(car_year,int),isinstance(conv,bool)].count(True) == 3:
            return {"brand": car_brand, "model": car_model, "production_year": car_year, "convertible": conv}
        else:
            print("Check the type of parameters:\n","{'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }")
            return None


def add_car():
    new_car_dict = input_car_data(True)
    if new_car_dict:    
        try:
            add_reply = requests.post("http://localhost:3000/cars/", headers = json_type, data = json.dumps(new_car_dict))
        except requests.RequestException as e:
            print(e.message)
        else:
            if add_reply.status_code == requests.codes.ok or add_reply.status_code == requests.codes.created:
                print("Success!")
                update_car_ids()
            elif add_reply.status_code == requests.codes.not_found:
                print("Not found")
            else:
                print("Can't add a car. Check the status code: ",add_reply.status_code)
                
    


def update_car():
    car_id = enter_id()
    if car_id is None:
        return None
    update_car_ids()
    if car_id not in car_ids:
        print("There is no car with such ID.Try again")
        return None   
    if check_server(car_id):
        update_car_dict = {"id":car_id}
        dict_input = input_car_data(False)

        if dict_input is not None:
            update_car_dict = {**update_car_dict,**dict_input}
        else:
            return None
        
        try:
            update_reply = requests.put("http://localhost:3000/cars/" + str(car_id), headers = json_type, data = json.dumps(update_car_dict))
        except requests.RequestException as e:
            print(e.message)
        else:
            if update_reply.status_code == requests.codes.ok:
                print("Success!")
                update_car_ids()
            elif update_reply.status_code == requests.codes.not_found:
                print("Not found")
            else:
                print("Can't add the item")
        
#Programm launch
while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
        #print(car_ids)
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
