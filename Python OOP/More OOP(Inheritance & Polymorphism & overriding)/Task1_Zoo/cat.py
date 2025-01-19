from animals import animals
class cat(animals):
    def __init__(self,name,age,gender,happinesslevel,healthlevel,voiceName):
        super().__init__(name,age,gender,happinesslevel,healthlevel)
        self.voiceName=voiceName
        
        
    def display_info(self):
        print(f"name:{self.name} age:{self.age} gender:{self.gender}, happinesslevel:{self.happinesslevel} healthlevel{self.healthlevel}, voiceName: {self.voiceName}")

        
            