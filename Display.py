import pandas as pd
import os
import re
from Cal import Cal

def Display():
    date=input('วันที่ที่ต้องการค้นหา:')
    file = open("Data.txt","r")
    count = 0
    line = 0
    x = file.readlines()
    b = len(x)
    CashM = []
    CashP = []
    Datelist = []
    DTlist = []
    Total =[]
    #print(x[count])
    #print(x[b-1])
    for i in range(1,b+1):
        file = open("Data.txt","r")
        Sentense = file.read().splitlines()
        SentenseCount = Sentense[count]
        StrSentense = str(SentenseCount)
        Date = StrSentense.split(" ")[0]
        if date == Date :
            C = count
            Datelist.append(Date)
            Money_DT = StrSentense.partition(" ")[2]
            Money = Money_DT.partition(" ")[0] 
            DT = Money_DT.partition(" ")[2] #Description
            DTlist.append(DT)
            #print(Money_DT)
            #print(DT)
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
    colsname = {
        'Date' : Datelist,
        'Description' : DTlist,
        'Income' : CashP,
        'Expense' : CashM,
        'total' : Total
        }
    print(pd.DataFrame(colsname))
    print(C)
    
while True :
    Display()
