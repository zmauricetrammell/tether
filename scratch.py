"""
Component is the parent class for the other classes
Component will hold metadata and the show methods.
"""
class Component:
    def __init__(self,name,description):
        self.name = name 
        self.description = description

    def show(self):
        print("Name: {} | Description: {}".format(self.name,self.description))

"""
This class is the location component of the program.

Beacons correspond to a location in the user's environment, they have 
standard component metadata and additional location and code attributes.
Beacons are used to track where the larger action object will require 
the user to be. Beacons have RFID tags that will be scanned to initiate 
and conclude actions.
"""
class Beacon(Component):
    def __init__(self, name, description, location, code = '0000'):
        super().__init__(name, description)
        self.location = location
        self.code = code

    def show(self):
        print("Name: {} | Description: {} | Location: {} | Code: {}".format(self.name,self.description, self.location, self.code))

    def scan(self): # wait for RFID to be scanned
        match = False

        while not match:
            print("Scanning...") 
            inputString = input() # TODO build in RFID scanner
            print("Code received: {}".format(inputString))

            if(inputString == self.code): # compare code received to code cached for beacon
                match = True
                print("Pass")
            else:
                print("Fail")

            
""" 
This class is the basic component of the program
*Actions* -> Tasks -> Routines
"""
class Action(Component):
    def __init__(self, name, description):
        super().__init__(name, description)
 
""" 
This class is the intermediary component of the program
Actions -> *Tasks* -> Routines
"""
class Task(Component):
    def __init__(self, name, description, actions: list):
        super().__init__(name, description)
        self.actions = actions

    def show(self):
        print("Name: {} | Description: {} | Actions: {}".format(self.name,self.description, self.actions))


def main(): 
    
    testComponent = Component("test component","test component description")
    #testComponent.show()

    testBeacon = Beacon("test beacon","test beacon description","test location")
    #testBeacon.show()
    testBeacon.scan()

    testAction = Action("test action","test action description")
    #testAction.show()

    testTask = Task("test task", "test task description",[testAction,testAction])
    #testTask.show()
    
   
# __name__ 
if __name__=="__main__": 
    main()