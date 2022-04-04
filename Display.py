import pandas as pd

def Display():
    
    date=input('วันที่ต้องการค้นหา:')
    file = ("Data.txt","a+")
    with open(file) as f :
        line = f.readline()
        cnt = 1
        while line:

        a = 200
        b = 100
        describe = "k"
    colsname = {
        'Date' : [date],
        'Description' : [describe],
        'Income' : [a],
        'Expense' : [b],
        'total' : [a-b]

    }
    print(pd.DataFrame(colsname))
