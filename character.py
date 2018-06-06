import numpy as np
import copy as cp
from dicepool import dpool
from attributes import Attributes
from skills import Skills
from health import Health

class Character(object):
    """
    Class holding the character
    """
    def __init__(self,
                 skills = Skills(), attributes = Attributes(), health = Health()
                 ):
        self.skills = skills
        self.attributes = attributes
        self.health = health

    def finish(self):
        self.attributes.finish()
        self.skills.finish()


    def skill(self, skill):
        return self.skills.skill(skill)

    def attribute(self, attribute):
        return self.attributes.attribute(attribute)





if __name__ == "__main__":

    ch = Character()

    ch.finish()

    print(
        ch.skill('academics'), ch.skill('computer'), ch.skill('crafts'), ch.skill('investigation'),
        ch.skill('medicine'), ch.skill('occult'), ch.skill('politics'), ch.skill('science'),
        ch.skill('athletics'), ch.skill('brawl'), ch.skill('drive'), ch.skill('firearms'), ch.skill('larceny'),
        ch.skill('stealth'), ch.skill('survival'), ch.skill('weaponry'), ch.skill('animal_ken'),
        ch.skill('empathy'), ch.skill('expression'), ch.skill('intimidation'), ch.skill('persuasion'),
        ch.skill('socialize'), ch.skill('streetwise'), ch.skill('subterfuge')
        )

