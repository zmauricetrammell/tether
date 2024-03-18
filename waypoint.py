from component import Component
from random import randint

Waypoints = {}

"""
This class is the location component of the program.

Waypoints correspond to a location in the user's environment, they have 
standard component metadata and additional location and code attributes.
Waypoints are used to track where the larger action object will require 
the user to be. Waypoints have RFID tags that will be scanned to initiate 
and conclude actions.
"""

class Waypoint(Component): 
    def __init__(self, name, description, location):
        super().__init__(name, description)
        self.location = location
        self.code = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])


    def toString(self):
        return("Name: {} | Description: {} | Location: {} | Code: {}".format(self.name,self.description, self.location, self.code))
    
    def do(self):
        print(self.toString()) 
        print()
        self.scan()

    def scan(self): # waits for RFID to be scanned
        match = False
        while not match: # TODO Move this to main.py
            input_string = input("Waypoint Code: ") # TODO build in RFID scanner

            if(input_string == self.code): # compare code received to code cached for Waypoint
                match = True
                print("Pass")
            else:
                print("Fail")

def main(): 

    #testWaypoint = createWaypoint()
    test_waypoint = Waypoint("test Waypoint","test Waypoint description","test location")
    print(test_waypoint.toString())
    test_waypoint.scan()
    
   
# __name__ 
if __name__=="__main__": 
    main()