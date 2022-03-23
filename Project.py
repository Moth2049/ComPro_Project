#Menu Function
from Enter_item import EI #Function1

while True :
    print("1. Enter item")
    print("2. Display")
    print("3. Save")
    print("4. Load")
    print("5. Delete")
    item = int(input("Please select the menu : "))
    
    if item == 1 :
        EI()

 
