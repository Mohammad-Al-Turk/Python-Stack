from animals import animals

class lion(animals):
    def __init__(self,name,age,gender,happinesslevel,healthlevel,power):
        super().__init__(name,age,gender,happinesslevel,healthlevel)
        self.power=power
        
        
    def display_info(self):
        print(f"name:{self.name} age:{self.age} gender:{self.gender}, happinesslevel:{self.happinesslevel} healthlevel{self.healthlevel} ")
  
            