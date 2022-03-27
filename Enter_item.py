def EI():
    #Extract word from sentense Complete!
    A = str(input("what do u need : "))
    Date = A.partition(" ")[0]
    Money = A.partition(" ")[2]
    Cash = Money.partition(" ")[0] 
    DT = Money.partition(" ")[2] #Description

    #Extract Date Complete!
    Day = Date.partition("/")[0]
    MY = Date.partition("/")[2] #Extract Month and Year
    Month = MY.partition("/")[0]
    Year = MY.partition("/")[2]
    
    #Write flie Complete!
    file = open("Data.txt","r+")    #Read and write at the same time
    file.write(A + "\n")
    
