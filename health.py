from dicepool import dpool

class Health(object):
    """
    Class holding the character
    """
    def __init__(self, maxHP = 7):
        self.maxHP = maxHP
        self.dmg = {}
        self.fully_heal()

    def fully_heal(self):
        self.dmg['bashing'] = 0
        self.dmg['lethal'] = 0
        self.dmg['aggravated'] = 0
        self.conscious = True
        self.alive = True

    def turn(self, stamina):
        self.instant_effects()
        
        # mortal risking unconscious
        if self.dmg['lethal'] + self.dmg['aggravated'] < self.maxHP and \
           self.dmg['lethal'] + self.dmg['aggravated'] + self.dmg['bashing'] >= self.maxHP:
               roll = dpool(stamina)
               if roll <= 0:
                   self.conscious = False
            
    def instant_effects(self):
        self.convert()
        
        # mortal death check
        if self.dmg['aggravated'] >= self.maxHP:
            self.alive = False
            self.conscious = False
        

    def hit(self, dmg, dmg_type):
        self.dmg[dmg_type] = self.dmg[dmg_type] + dmg
        self.instant_effects()

    def convert(self):
        total = self.dmg['bashing'] + self.dmg['lethal'] + self.dmg['aggravated']

        while self.dmg['bashing'] > 0 and total > self.maxHP and self.dmg['lethal'] < self.maxHP:
            self.dmg['lethal'] = self.dmg['lethal'] + 1
            self.dmg['bashing'] = self.dmg['bashing'] - 2
            total = total - 1

        while self.dmg['bashing'] > 0 and total > self.maxHP and self.dmg['aggravated'] < self.maxHP:
            self.dmg['aggravated'] = self.dmg['aggravated'] + 1
            self.dmg['bashing'] = self.dmg['bashing'] - 1
            self.dmg['lethal'] = self.dmg['lethal'] - 1
            total = total - 1

        while self.dmg['lethal'] > 0 and total > self.maxHP:
            self.dmg['aggravated'] = self.dmg['aggravated'] + 1
            self.dmg['lethal'] = self.dmg['lethal'] - 2
            total = total - 1


class VampireHealth(Health):
    def fully_heal(self):
        super(VampireHealth, self).fully_heal()
        self.torpor = False
        
    def hit(self, dmg, dmg_type):
        if dmg_type == 'lethal':
            dmg_type = 'bashing'
            
        super(VampireHealth, self).hit(dmg=dmg, dmg_type=dmg_type)
        
    def instant_effects(self):
        self.convert()
        
        # vampire goes to torpor
        if self.dmg['lethal'] + self.dmg['aggravated'] >= self.maxHP:
            self.conscious = False
            self.torpor = True
                   
        # vampire death check
        if self.dmg['aggravated'] >= self.maxHP:
            self.alive = False
            self.conscious = False
        
    def turn(self, stamina):
        self.instant_effects()
        


if __name__ == "__main__":
    he = Health()
    he = VampireHealth()

    he.hit(dmg=9, dmg_type='bashing')
    he.hit(dmg=2, dmg_type='lethal')
    
    for i in range(0,10):
        print(he.conscious)
        he.turn(stamina=3)
    
    print(he.dmg['aggravated'], he.dmg['lethal'], he.dmg['bashing'])
    
    he.hit(dmg=15, dmg_type='lethal')
    
    print(he.dmg['aggravated'], he.dmg['lethal'], he.dmg['bashing'])
    print(he.conscious, he.alive, he.torpor)
    
    he.fully_heal()
    
    print(he.dmg['aggravated'], he.dmg['lethal'], he.dmg['bashing'])
    print(he.conscious, he.alive)



