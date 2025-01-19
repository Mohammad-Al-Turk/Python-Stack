from animals import animals
class dog(animals):
    def __init__(self,name,age,gender,happinesslevel,healthlevel,speed):
        super().__init__(name,age,gender,happinesslevel,healthlevel)
        self.speed=speed
        
        
    def display_info(self):
        print(f"name:{self.name} age:{self.age} gender:{self.gender}, happinesslevel:{self.happinesslevel} healthlevel{self.healthlevel}, speed:{self.speed}")

        
            