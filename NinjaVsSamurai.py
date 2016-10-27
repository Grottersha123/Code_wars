Position = {'high': 'h','low': 'l'}

class Warrior():
    def __init__(self,name,health = 100):
        #each warrior should be created with a name and 100 health points
        self.deceased = False
        self.zombie = False
        self.name=name
        self.health=health
        #default guard is "", that is unguarded
        self.block=""
        
    def attack(self,enemy,position):
        damage = 0
        #attacking high deals 10 damage, low 5
        #0 damage if the enemy blocks in the same position
        if enemy.block!=position: damage+=10 if position==Position['high'] else 5
        #and even more damage if the enemy is not blocking at all
        if enemy.block=="": 
            damage+=5
        enemy.set_health(enemy.health-damage)
    
    def set_health(self,new_health):        
        #health cannot have negative values
        self.health=min(self.health,new_health)
        #if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased=True
            self.zombie=False
        #he would be a zombie only if he was already dead
        if self.health  < 0: 
            self.zombie=True
