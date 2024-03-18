from consolemenu import *
from consolemenu.items import *

menu_list = ["A","B","C"]

# Create menu
menu = ConsoleMenu("Title","Subtitle")

#selection_menu = SelectionMenu(["A","B","C"])
# Create items

def makeMenu():
    function_item = FunctionItem("Make a Menu",menu.append_item,[MenuItem("Test")])
    return function_item

# Function items run functions when selected
#function_item = FunctionItem("Call a Python function",input, ["Enter an input"])

menu.append_item(makeMenu())

#submenu_item = SubmenuItem("Submenu item",selection_menu,menu)
#menu.append_item(submenu_item)
menu.show()