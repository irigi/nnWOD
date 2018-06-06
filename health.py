import numpy as np
import copy as cp
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

    def hit(self, dmg, dmg_type):
        self.dmg[dmg_type] = self.dmg[dmg_type] + dmg
        self.convert()
        return

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


if __name__ == "__main__":
    he = Health()

    he.hit(dmg=14, dmg_type='bashing')
    he.hit(dmg=2, dmg_type='lethal')
    print(he.dmg['aggravated'], he.dmg['lethal'], he.dmg['bashing'])



