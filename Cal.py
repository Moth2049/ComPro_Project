def Cal(k):
    file = open("Data.txt","r")
    count = 0
    A=0
    B=0
    total = 0
    for i in range(1,k+1):
        file = open("Data.txt","r")
        file = open("Data.txt","r")
        Sentense = file.readlines()
        SentenseCount = Sentense[count]
        StrSentense = str(SentenseCount)
        Money_DT = StrSentense.partition(" ")[2] #Money and Description
        Money = Money_DT.partition(" ")[0] #Money
        if "+" in Money:
            CashPl = Money.partition("+")[2]
            CashP = int(CashPl)
            A=A+CashP
        elif "-" in Money:
            CashMi = Money.partition("-")[2]
            CashM = int(CashMi)
            B=B-CashM
      
        count += 1
    total = total+A+B 
    return total

    
