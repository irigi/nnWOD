import numpy as np
import copy as cp
from dicepool import dpool

class Skills(object):
    """
    Class holding the attributes of a character
    """
    def __init__(self,
                 academics = 0, computer = 0, crafts = 0, investigation = 0,
                 medicine = 0, occult = 0, politics = 0, science = 0,
                 athletics = 0, brawl = 0, drive = 0, firearms = 0, larceny = 0,
                 stealth = 0, survival = 0, weaponry = 0,
                 animal_ken = 0, empathy = 0, expression = 0, intimidation = 0,
                 persuasion = 0, socialize = 0, streetwise = 0, subterfuge = 0
                 ):
        self.skills = {}

        self.list = {}
        self.list['physical'] = ['academics', 'computer', 'crafts', 'investigation',
        'medicine', 'occult', 'politics', 'science']

        self.list['psychical'] = ['athletics', 'brawl', 'drive', 'firearms',
        'larceny', 'stealth', 'survival', 'weaponry']

        self.list['social'] = ['animal_ken', 'empathy', 'expression', 'intimidation',
        'persuasion', 'socialize', 'streetwise', 'subterfuge']

        self.skills['academics'] = academics
        self.skills['computer'] = computer
        self.skills['crafts'] = crafts
        self.skills['investigation'] = investigation
        self.skills['medicine'] = medicine
        self.skills['occult'] = occult
        self.skills['politics'] = politics
        self.skills['science'] = science

        self.skills['athletics'] = athletics
        self.skills['brawl'] = brawl
        self.skills['drive'] = drive
        self.skills['firearms'] = firearms
        self.skills['larceny'] = larceny
        self.skills['stealth'] = stealth
        self.skills['survival'] = survival
        self.skills['weaponry'] = weaponry

        self.skills['animal_ken'] = animal_ken
        self.skills['empathy'] = empathy
        self.skills['expression'] = expression
        self.skills['intimidation'] = intimidation
        self.skills['persuasion'] = persuasion
        self.skills['socialize'] = socialize
        self.skills['streetwise'] = streetwise
        self.skills['subterfuge'] = subterfuge

    def get_sum(self, name):
        return sum([self.skills[key] for key in self.list[name]])

    def get_sum_psychical(self):
        return self.get_sum('psychical')

    def get_sum_physical(self):
        return self.get_sum('physical')

    def get_sum_social(self):
        return self.get_sum('social')

    def finish(self):
        for key in self.list:
            while self.get_sum(name=key) < 4:
                sk = np.random.choice(self.list[key])
                self.skills[sk] = self.skills[sk] + 1


        rem = []
        for key in self.list:
            if self.get_sum(key) == 4:
                rem.append(key)

        selected = np.random.choice(rem)

        remaining = [key for key in self.list]
        remaining.remove(selected)

        for key in remaining:
            while self.get_sum(name=key) < 7:
                sk = np.random.choice(self.list[key])
                self.skills[sk] = self.skills[sk] + 1


        rem = []
        for key in remaining:
            if self.get_sum(key) == 7:
                rem.append(key)

        selected = np.random.choice(rem)
        remaining.remove(selected)

        for key in remaining:
            while self.get_sum(name=key) < 11:
                sk = np.random.choice(self.list[key])
                self.skills[sk] = self.skills[sk] + 1


    def missing(self):
        physical = self.get_sum_physical()
        psychical = self.get_sum_psychical()
        social = self.get_sum_social()

        maximum = max(physical, psychical, social)
        minimum = min(physical, psychical, social)
        middle = physical + psychical + social - minimum - maximum

        return maximum - 11, middle - 7, minimum - 4

    def skill(self, skill):
        return self.skills[skill]





if __name__ == "__main__":

    sk = Skills()

    print(sk.get_sum_psychical())
    print(sk.get_sum_social())
    print(sk.get_sum_physical())

    sk.finish()

    print(sk.get_sum_psychical())
    print(sk.get_sum_social())
    print(sk.get_sum_physical())

    print(
        sk.skill('academics'), sk.skill('computer'), sk.skill('crafts'), sk.skill('investigation'),
        sk.skill('medicine'), sk.skill('occult'), sk.skill('politics'), sk.skill('science'),
        sk.skill('athletics'), sk.skill('brawl'), sk.skill('drive'), sk.skill('firearms'), sk.skill('larceny'),
        sk.skill('stealth'), sk.skill('survival'), sk.skill('weaponry'), sk.skill('animal_ken'),
        sk.skill('empathy'), sk.skill('expression'), sk.skill('intimidation'), sk.skill('persuasion'),
        sk.skill('socialize'), sk.skill('streetwise'), sk.skill('subterfuge')
        )

    print (sk.missing())

