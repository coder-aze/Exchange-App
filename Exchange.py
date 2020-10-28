import requests
import json

class Exchange:
    data="https://api.exchangeratesapi.io/{}?base={}"
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def latest(self,much):
        data=self.data.format("latest",self.val1)
        result=json.loads(requests.get(data).text)
        print(1,self.val1,"===",result["rates"][self.val2],self.val2)
        print("-------------------------")
        print(much,self.val1,"===",result["rates"][self.val2]*much,self.val2)
        print()
    def specific_time(self,much):
        year=input("YEAR:  ")
        month=input("MONTH:  ")
        day=input("DAY:  ")
        time=year+"-"+month+"-"+day
        data=self.data.format(time,self.val1)
        result=json.loads(requests.get(data).text)
        print()
        print("DATE: ",time)
        print("-------------------------")
        print(1,self.val1,"===",result["rates"][self.val2],self.val2)
        print("-------------------------")
        print(much,self.val1,"===",result["rates"][self.val2]*much,self.val2)
        print()

while True:
    ans=input("1-LAST CURRENCY\n2-CURRENCY AT A SPECIFIC TIME:  ")
    if ans=="1":
        val1=input("FIRST VALUE: ")
        print("to...")
        val2=input("LAST VALUE: ")
        much=int(input("MUCH: "))
        test=Exchange(val1,val2)
        test.latest(much)
    elif ans=="2":
        val1=input("FIRST VALUE: ")
        print("to...")
        val2=input("LAST VALUE: ")
        much=int(input("MUCH: "))
        test=Exchange(val1,val2)
        test.specific_time(much)