def EI():

    Word = str(input("what do u need : "))
    file = open("Data.txt","a+")    #Write at new line
    file.write(Word+"\n")
    file.close
