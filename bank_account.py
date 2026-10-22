from datetime import datetime, date,timezone
from zoneinfo import ZoneInfo
class BankAccount:
    def __init__(self,account_number,owner_name,balance=0):
        self.transaction_history=[]
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
    def view_data(self):
        for i in range(len(self.transaction_history)):
            self.transaction_history[i].return_data()       
    def deposit(self,amount):
        self.balance+=amount
        now = datetime.now(timezone.utc)
        dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
        change=Transaction("deposit",amount,dt_new)
        self.transaction_history.append(change)
        print(" An amount of "+str(amount)+" dollars has been deposited into "+self.owner_name+"'s account. The new balance is "+str(self.balance)+" ")
    def withdrawl(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            now = datetime.now(timezone.utc)
            dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
            change=Transaction("withdrawl",amount,dt_new)
            self.transaction_history.append(change)
            print(" An amount of "+str(amount)+" dollars has been withdrawled from "+self.owner_name+"'s account. The new balance is "+str(self.balance)+" ")    
        else:
            print("You can not wihdrawl more money than in your account")
    def get_balance(self):
        print("$"+str(self.balance)+"")         
    def transfer_funds(self,other_account,amount):
        if self.balance>=amount:
            self.balance-=amount
            other_account.balance+=amount
            now = datetime.now(timezone.utc)
            dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
            change=Transaction("transfer",amount,dt_new)
            self.transaction_history.append(change)
            other_account.balance+=amount
            print(" "+str(amount)+" dollars has been transfered from one account to the other ")
        else:
            print("You can not transfer more money than you own")    
        
class SavingsAccount(BankAccount):
    def __init__(self,account_number,owner_name,minimum_balance,interest_rate,balance=0):
        super().__init__(account_number,owner_name,balance=0)    
        self.interest_rate=interest_rate
        self.minimum_balance=minimum_balance
    def apply_interest(self):
        self.balance+=self.balance*self.interest_rate
        now = datetime.now(timezone.utc)
        dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
        change=Transaction("Interest Applied",self.interest_rate,dt_new)
        self.transaction_history.append(change)
        print(self.balance)
    def withdrawl(self,amount):
        if self.balance-amount>=self.minimum_balance:
            self.balance-=amount
            now = datetime.now(timezone.utc)
            dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
            change=Transaction("withdrawl",amount,dt_new)
            self.transaction_history.append(change)
            print(" An amount of "+str(amount)+" dollars has been withdrawled from "+self.owner_name+"'s account. The new balance is "+str(self.balance)+" ")    
        else:
            print("Your balance can not go below the mininum")
class CheckingAccount(BankAccount):
    def __init__(self,account_number,owner_name,overdraft_limit,balance=0):
        super().__init__(account_number,owner_name,balance=0)    
        self.overdraft_limit=overdraft_limit
    def withdrawl(self,amount):
        if self.balance-amount>self.overdraft_limit:
            self.balance-=amount
            now = datetime.now(timezone.utc)
            dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
            change=Transaction("withdrawl",amount,dt_new)
            self.transaction_history.append(change)
            print(" An amount of "+str(amount)+" dollars has been withdrawled from "+self.owner_name+"'s account. The new balance is "+str(self.balance)+" ")    
        else:
            print("Overdraft")
            self.balance-=5
            now = datetime.now(timezone.utc)
            dt_new=now.astimezone(ZoneInfo("America/Los_Angeles"))
            change=Transaction("overdraft fee",5,dt_new)
            self.transaction_history.append(change)
class Transaction:
    def __init__(self,type,amount,time):
        self.type=type
        self.amount=amount
        self.time=time    
    def return_data(self):
        readable_dt=self.time.strftime("%A, %B %d, %Y at %I:%M %p")
        print(" The transaction was a "+self.type+" made at "+readable_dt+" of an amount of "+str(self.amount)+" dollars ")
account=BankAccount("1","John")        
saccount=SavingsAccount("2","John",10,0.15)
caccount=CheckingAccount("3", "John",-5)
account.deposit(200)
account.withdrawl(123)
account.transfer_funds(saccount,39)
saccount.apply_interest()
saccount.withdrawl(30)
caccount.deposit(300)
caccount.withdrawl(301)
caccount.withdrawl(5)
account.view_data()
saccount.view_data()
caccount.view_data()
