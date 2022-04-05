def Cal(k):
    file = open("Data.txt","r")
    count = 0
    line = 0
    x = file.readlines()
    b = len(x)
    z=0
    y=0
    c=0
    d=0
    total = 0
    for i in range(1,k+1):
        file = open("Data.txt","r")
        file = open("Data.txt","r")
        Sentense = file.readlines()
        SentenseCount = Sentense[count]
        StrSentense = str(SentenseCount)
        Date = StrSentense.split(" ")[0]
        Money_DT = StrSentense.partition(" ")[2]
        Money = Money_DT.partition(" ")[0] 
        if "+" in Money:
            CashPl = Money.partition("+")[2]
            z = int(CashPl)
            c=c+z
        elif "-" in Money:
            CashMi = Money.partition("-")[2]
            y = int(CashMi)
            d=d-y
      
        count += 1
    total = total+c+d 
    print(total)
    return total

    
