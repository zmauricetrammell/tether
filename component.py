"""
Components

Components are a shell parent class that have metadata fields.

- Component Name
- Component Description
"""

class Component:
    def __init__(self,name,description):
        self.name = name 
        self.description = description

    def toString(self):
        print("{}: {}".format(self.name,self.description))
   
def main(): 
    testComponent = Component("test","test component description")
    testComponent.toString()
   
# __name__ 
if __name__=="__main__": 
    main()