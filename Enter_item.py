def EI():
    A = str(input("what do u need : "))
    Date = A.partition(" ")[0]
    Money = A.partition(" ")[1]
    DT = A.partition(" ")[2] #Description
    print(Date)
    print(Money)
    print(DT)
