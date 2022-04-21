#Menu Function
from Display import Display
from Display import Load
from Enter_item import EI
a = 1
while a == 1:
    print("1. Enter item")
    print("2. Display")
    print("3. Load")
    print("4. Exit")
    item = str(input("Please select the menu : "))
    
    if item == "1" :
        EI()
    if item == "2" :
        Display()
    if item == '3' :
        Load()
    #Exit 
    if item == "4" :
        a += 1 
    
