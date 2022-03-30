def EI():
    #Extract word from sentense Complete!
    Word = str(input("what do u need : "))
    Date = Word.partition(" ")[0]
    Money_DT = Word.partition(" ")[2]
    Money = Money_DT.partition(" ")[0] 
    DT = Money_DT.partition(" ")[2] #Description
    if "+" in Money :
        CashP = Money.partition("+")[2]
        FileCP = open("CashP.txt","a+")
        FileCP.write(CashP+"\n")
        FileCP.close
    elif "-" in Money :
        CashM = Money.partition("-")[2]
        FileCM = open("CashM.txt","a+")
        FileCM.write(CashM+"\n")
        FileCM.close


    #Extract Date Complete!
    Day = Date.partition("/")[0]
    MY = Date.partition("/")[2] #Extract Month and Year
    Month = MY.partition("/")[0]
    Year = MY.partition("/")[2]
    
    FileD = open("Date.txt","a+")
    FileD.write(Date+"\n")
    FileD.close
    
    #Write flie Complete!
    file = open("Data.txt","a+")    #Read and write at the same time
    file.write(Word+"\n")
    file.close
    
   
