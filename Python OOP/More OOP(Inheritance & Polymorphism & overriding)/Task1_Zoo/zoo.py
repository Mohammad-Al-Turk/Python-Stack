from cat import cat
from lion import lion
from dog import dog
from animals import *


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_lion(self, lion):
        self.animals.append(lion)
        
    def cat(self, cat):
        self.animals.append(cat)
        
    def dog(self, dog):
        self.animals.append(dog)

        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
            
zoo1=Zoo("John's Zoo")
fofo=lion('fofo', 12, 'f', 100, 100, 100)
zoo1.add_lion(fofo)
zoo1.print_all_info()

