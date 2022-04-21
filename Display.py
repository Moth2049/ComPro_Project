import pandas as pd
from Cal import Cal

def Display():
    date=input('วันที่ที่ต้องการค้นหา:')
    file = open("Data.txt","r")
    count = 0
    #count line
    x = file.readlines()
    b = len(x)
    #create list
    CashM = []
    CashP = []
    Datelist = []
    DTlist = []
    Total =[]
    for i in range(1,b+1):
        file = open("Data.txt","r")
        Sentense = file.read().splitlines()
        SentenseCount = Sentense[count] #read line [x]
        StrSentense = str(SentenseCount) #make it to string
        Date = StrSentense.split(" ")[0] # Extract Date
        if date == Date :
            Datelist.append(Date)
            Money_DT = StrSentense.partition(" ")[2] #Money and Description
            Money = Money_DT.partition(" ")[0] #Money
            DT = Money_DT.partition(" ")[2] #Description
            DTlist.append(DT)
            if "+" in Money:
                CashPl = Money.partition("+")[2]
                CashP.append(CashPl)
                CashMi = 0
                CashM.append(CashMi)
                
            elif "-" in Money:
                CashMi = Money.partition("-")[2]
                CashM.append(CashMi)
                CashPl = 0
                CashP.append(CashPl)
            total = Cal(count+1)
            Total.append(total)  
    
        count += 1
    if date in Datelist : 
        #create colums
        colsname = {
            'Date' : Datelist,
            'Description' : DTlist,
            'Income' : CashP,
            'Expense' : CashM,
            'total' : Total
            }
        print(pd.DataFrame(colsname))
    if date not in Datelist :
        print("Sorry, This date doesn't exist") 
    
#month
def Load():
    Month=input('เดือนที่ต้องการค้นหา:')
    file = open("Data.txt","r")
    count = 0
    #count line
    x = file.readlines()
    b = len(x)
    #create list
    CashM = []
    CashP = []
    Monthlist = []
    Daylist = []
    Descriptionlist = []
    Total = []
    for i in range(1,b+1):
        file = open("Data.txt","r")
        Sentense = file.read().splitlines()
        SentenseCount = Sentense[count] #read line [x]
        StrSentense = str(SentenseCount) #make it to string
        Date = StrSentense.partition(" ")[0] # Extract Date
        month = Date.partition("/")[2]
        RealMonth = month.partition("/")[0]
        if Month == RealMonth :
            day = Date.partition("/")[0]
            Daylist.append(day)
            Monthlist.append(RealMonth)
            Money_DT = StrSentense.partition(" ")[2] #Money and Description
            Money = Money_DT.partition(" ")[0] #Money
            DT = Money_DT.partition(" ")[2] #Description
            Descriptionlist.append(DT)
            if "+" in Money:
                CashPl = Money.partition("+")[2]
                CashP.append(CashPl)
                CashMi = 0
                CashM.append(CashMi)
                
            elif "-" in Money:
                CashMi = Money.partition("-")[2]
                CashM.append(CashMi)
                CashPl = 0
                CashP.append(CashPl)
            total = Cal(count+1)
            Total.append(total)  
    
        count += 1
    if Month in Monthlist : 
        a = 'All in month'
        #create colums
        colsname = {
            'Month' : [Month],
            'Description' : [a],
            'total' : [total]
            }
        print(pd.DataFrame(colsname))
        B = str(input('Do you want lists of date? (Y/n):'))
        if 'Y' in B :
            colsnames = {
            'Date' : Daylist,
            'Income' : CashP,
            'Expense' : CashM,
            'Description' : Descriptionlist,
            'total' : Total
            }
            print(pd.DataFrame(colsnames))
        else :
            nothing = 1

    if Month not in Monthlist :
        print("Sorry, This month doesn't exist") 
