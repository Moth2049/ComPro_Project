def EI():
    A = str(input("what do u need : "))
    Date = A.partition(" ")[0]
    Money = A.partition(" ")[2]
    Cash = Money.partition(" ")[0] 
    DT = Money.partition(" ")[2] #Description
    
    Day = Date.partition("/")[0]
    Month = Date.partition("/")[1]
    Year = Date.partition("/")[2]
    print(Date)
    print(Cash)
    print(DT)
    

