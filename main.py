# Create a program that will take schedual of incoming spaceships, each with different sizes and docking time
# requierments, and a map of available docking bays at a space station.
import random 
import dockingBays as db 

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()

# This function will take the schedule of the spaceship and list avalible bays based on the size of the ships
def schedule_ships():
# This string will save the bay 
    incoming_ships = random.choice(incoming_ships)
# This if else statement will go through each size and tell you which size bays are available 
    if 'Size' == 'small' in db.dockingBays:
        print(f"Docking bays vailable are {{Bay:['bay_id'], Size:['size'], time:['arrival_time'}}.")
    elif 'Size' == 'medium' in db.dockingBays:
        print(f"Docking bays vailable are {{Bay:['bay_id'], Size:['size'], time:['arrival_time']}}.")
    else 'Size' == 'large' in db.dockingBays:
        print(f"Docking bays vailable are {{Bay:['bay_id'], Size':['size], time:['arrival_time']}}.")
 

# This function will tell you which bays are aviable for the ships docking time window 
def list_of_bays():
    docking_bays = random.chice(docking_bays)
    incoming_ships = random.choice(incoming_ships)
#This for loop will go through each bay and see which one is open for its time window   
    for time in incoming_ships:
        for bays in docking_bay:
            if 'schedual' == open:
                print(f'Bay{['bay_id']} is open')   


# This function will assign ships a bay based on size and time 
def assign_bays():
    incoming_ships = random.choice(incoming_ships)
# This if else statment will go through all the requierments to assign each ship a bay
    if (size) & (time) in docking_bays:
        print(f"You are assinged bay {docking_bays}")
    elif (size) & (time) in dockign_bays:
        print(f"You are assinged bay {docking_bays}")



# This function will give the amout of times for each ship so that they leave on time so they dont stay to long and take up space
def optimized_time():
    incoming_ships = random.choice(incoming_ships)
    docking_bays = random.chice(docking_bays)
# This for loop wil go through each incoming ships and get the arrival time and give it the max amout of time it has to stay in that bay
    for ship in incoming_bays:
        for bay in docking_bays:
            if 'arrival_time' & 'departure_time' == docking_bays:
                print(f"You will be assigned bay {['bay_id']}")


# This will run the functions
schedule_ships()
list_of_bays()
assign_bays()
optimized_time()

        
            
     



















