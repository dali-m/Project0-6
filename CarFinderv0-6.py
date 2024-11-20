#CarFinder
#This program allows a user to find authorized vehicles sold.

AllowedVehiclesList = ['Ford F-150' , 'Chevrolet Silverado' , 'Tesla Cybertruck' , 'Toyota Tundra' , 'Nissan Titan' , 'Rivian R1T' , 'Ram 1500']
import os
file_name="./allowed_database.txt"
def init_file():
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            pass
    items = read_file()
    if len(items) == 0:
        with open(file_name,"w") as file:
            for vehicle in AllowedVehiclesList:
                file.write(vehicle+"\n")
                print(f"Adding {vehicle} to database")
            print(f"database has been initialized")
    else:
        print(f"file has already been initialized with {len(items)} items")

def read_file():
    with open(file_name,"r") as file:
        items = [line.strip() for line in file]
        return items
    return []

def add_to_file(vehicle_name):
    with open(file_name,"a+") as file:
        file.write(vehicle_name+"\n")

def remove_from_file(vehicle_name):
    vehicles = read_file()
    vehicles.remove(vehicle_name)
    with open(file_name, "w") as file:
        for vehicle in vehicles:
            file.write(vehicle+"\n")
            
            
#Adding the menu.
def print_menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.4')
    print('********************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. DELETE Authorized Vehicle')
    print('5. Exit')
    print('********************************')

#Adding the end part of the menu.
def print_all_vehicles():
    print('Authorized Vehicles:')
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print('*******************************')

#Defining search option.
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
     print(f"{vehicle_name} is an authorized vehicle")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print('********************************')

#Defining the Add option.
def add_vehicle(vehicle_name):
     if vehicle_name not in AllowedVehiclesList:
        AllowedVehiclesList.append(vehicle_name)
        print(f"You have added {vehicle_name} as an authorized vehicle.")

#Defining the DELETE option.
def remove_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f"Are you sure you want to remove '{vehicle_name}' from the Allowed Vehicles List? (yes/no): ")
        if confirmation == 'yes':        
            AllowedVehiclesList.remove(vehicle_name)
            print(f"You have REMOVED '{vehicle_name}' as an authorized vehicle.")
    else:
        print(f" '{vehicle_name}' not REMOVED as an authorized vehicle.")



#Second part of the menu 
def print_allowed_vehicles_list():
    print('\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicles in AllowedVehiclesList:
        print(vehicles)
    print('********************************')

#
def main():
    while True:
        print_menu()
        option = input()
        if option == '1':
            print_allowed_vehicles_list()
        elif option == '2':
            vehicle_name = input('Please Enter the full vehicle name:')
            search_vehicle(vehicle_name)
        elif option == '3':
            vehicle_name = input('Please Enter the full Vehicle name you would like to add:')
            add_vehicle(vehicle_name)
        elif option == '4':
            vehicle_name = input('Please Enter the full Vehicle name you would like to remove:')
            remove_vehicle(vehicle_name)
        elif option == '5':
            print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()