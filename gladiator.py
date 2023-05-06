class Gladiator:
    def __init__(self, name, hp, damage):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.damage = damage
        self.dead = False

    def info(self):
        print('name ', self.name, ' hp ', self.hp, ' damage ', self.damage)
        self.show_hp_graphically()

    def show_hp_graphically(self):
        print(('#' * self.hp) + ('-' * (self.maxHp - self.hp)))

    def is_dead(self):
        if self.hp <= 0:
            self.dead = True
            return True

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_hp(self, hp):
        if self.hp + hp <= self.maxHp:
            self.hp += hp
        else:
            self.hp = self.maxHp

    def attack(self, enemy):
        enemy.takeDamage(self.damage)


gladiator1 = Gladiator(1, 10, 2)
gladiator2 = Gladiator(1, 10, 2)

gladiator1.info()
gladiator2.info()
gladiator1.attack(gladiator2)
gladiator2.info()
print(gladiator2.is_dead())
gladiator2.get_hp(1)
gladiator2.info()
