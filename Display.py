import pandas as pd
account = {'จำนวนเงินในบัญชีผู้ใช้':0}

date=input('วันที่ต้องการค้นหา:')
describ=input('ใส่ข้อความที่ต้องการอธิบาย:')

def accountbalance():
    print ('ยอดเงินคงเหลือในบัญชี:',account)

def deposit(money):
    print ('ฝากเงินเข้าบัญชีผู้ใช้:',money)
    account['จำนวนเงินในบัญชีผู้ใช้']+=money
def expense(money):
    print ('ถอนเงินออกจากบัญชีผู้ใช้:',money)
    account['จำนวนเงินในบัญชีผู้ใช้']-=money

accountbalance()
deposit(300)
expense(100)
accountbalance()
#['Date','Description','Income','Expense','total']
''' 'Date' : print(date),
    'Description' : print(describ),
    'Income' : print(deposit()),
    'Expense' : print(expense()),
    'total' : print(accountbalance()) '''

colsname = {
    'Date' : [date],
    'Description' : [describ],
    'Income' : [deposit],
    'Expense' : [expense],
    'total' : [accountbalance]

}
print(pd.DataFrame(colsname))
