class Gladiator:
    Name = None
    hp = None
    damage = None
    dead = False
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def info(self):
        print('name ', self.name, ' hp ', self.hp, ' damage ', self.damage)
        
    def isDead(self):
        if self.hp <= 0:
            self.dead = True
            return True

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, enemy):
        enemy.takeDamage(self.damage)
        

gladiator1 = Gladiator(1, 10, 2)
gladiator2 = Gladiator(1, 10, 2)

gladiator1.info()
gladiator2.info()
gladiator1.attack(gladiator2)
gladiator2.info()
print(gladiator2.isDead())