class Monster: #Superclassa
    identity = "Antagonist"
    def __init__(self, name, color, heads): #magic methods/ dunder untis
        self.name= name
        self.color= color
        self.heads= heads
        
    def attack(self):
        print("Attack commencing")

#creating monsters
class Fogmonster(Monster):
    def make_sound(self):
        print("grrrrrr\n")
    def attack(self): #method overriding
        super().attack() #calling the super class method which is method of monster
        print("Kill commencing")
        
class SnekHead(Monster):
    def make_sound(self):
        print("hissssss\n")
        
class Kerberos(Monster): #HERE THE KERBERSOS CLASS INHERITED MONSTER
    def make_sound(self):
        print("Auuuuuuuu\n")
       
fogmonster = Fogmonster("Fogmonster","Grey",5)
print(f"A {fogmonster.heads} headed monster appeared that is {fogmonster.identity}")
fogmonster.make_sound()
fogmonster.attack()


