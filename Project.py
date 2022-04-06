#Menu Function
from Enter_item import EI #Function1
from Display import Display
a = 1
while a == 1:
    print("1. Enter item")
    print("2. Display")
    print("3. Exit")
    item = str(input("Please select the menu : "))
    
    if item == "1" :
        EI()
    if item == "2" :
        Display()
    if item == "3" :
        a == 2
    
