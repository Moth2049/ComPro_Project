import os
def EI():

    #Extract word from sentense Complete!
    Word = str(input("what do u need : "))
    Date = Word.partition(" ")[0]
    Money_DT = Word.partition(" ")[2]
    Money = Money_DT.partition(" ")[0] 
    DT = Money_DT.partition(" ")[2] #Description
    if "+" in Money:
        Cash = Money.partition("+")[2]
    if "-" in Money:
        Cash = Money.partition("-")[2]
    #Extract Date Complete!
    Day = Date.partition("/")[0]
    MY = Date.partition("/")[2] #Extract Month and Year
    Month = MY.partition("/")[0]
    Year = MY.partition("/")[2]
    
    #Write flie Complete!
    file = open("Data.txt","a+")    #Read and write at the same time
    file.write(Word+"\n")
    file.close

while True :
    EI()
    
    
   
