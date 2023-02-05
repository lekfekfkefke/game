class Player():
    def __init__(self, health, damage, armour):
        self.health = health
        self.damage = damage
        self.armour = armour

    def Parametrs(self):
        print(f"Здоровье: {self.health}, урон: {self.damage}, броня: {self.armour}")

    def Attack(self, opponent):
        opponent.health = opponent.health - self.damage * (1 - opponent.armour / 100)

player1=Player(100, 10,50)
player2=Player(100, 15,40)

i = 1

while player1.health > 0 and player2.health > 0:
    print(f"Ход №{i}")
    player1.Attack(player2)
    player2.Attack(player1)
    print(f"Здоровье игрока 1: {player1.health}, здоровье игрока 2: {player2.health}")
    i+=1

if player2.health < 0:
    print("Игрок 1 победил!")
if player1.health < 0:
    print("Игрок 2 победил!")