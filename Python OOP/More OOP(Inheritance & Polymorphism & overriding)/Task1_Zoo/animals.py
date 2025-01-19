class animals:
    def __init__(self,name,age,gender,happinesslevel,healthlevel):
        self.name=name
        self.age=age
        self.gender=gender
        self.happinesslevel=happinesslevel
        self.healthlevel=healthlevel
     
        
        
    def display_info(self):
        print(f"name:{self.name} age:{self.age} gender:{self.gender}, happinesslevel:{self.happinesslevel} healthlevel{self.healthlevel} ")

    
    def feednew(self):
        self.happinesslevel+=10
        self.healthlevel+=10
        