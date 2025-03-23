class Fruits:
    def __init__(self,nm,ctg):
        self.name=nm
        self.category=ctg
        self.list=[]
        
        
    def display(self):
        print("enter ")
        print(f" you name is {self.name} \n you category number are {self.category}")
    
    def addfruits(self,list):
        z=int(input("how namy fruits category u need"))
        list=input("kindly enter the fruitsname one by one")
        for i in range(z):
            self.insert(list)
            
                 
        
   
ft=Fruits("Ahsan",5)
ft.addfruits("banana")