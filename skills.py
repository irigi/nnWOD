import numpy as np
import matplotlib.pyplot as plt
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
        self.__academics = academics 
        self.__computer = computer 
        self.__crafts = crafts 
        self.__investigation = investigation 
        self.__medicine = medicine 
        self.__occult = occult 
        self.__politics = politics 
        self.__science = science
        self.__athletics = athletics 
        self.__brawl = brawl 
        self.__drive = drive 
        self.__firearms = firearms 
        self.__larceny = larceny 
        self.__stealth = stealth 
        self.__survival = survival 
        self.__weaponry = weaponry
        self.__animal_ken = animal_ken 
        self.__empathy = empathy 
        self.__expression = expression 
        self.__intimidation = intimidation 
        self.__persuasion = persuasion 
        self.__socialize = socialize 
        self.__streetwise = streetwise 
        self.__subterfuge = subterfuge 
        
    def missing(self):
        physical = self.Str() + self.Dex() + self.Sta()
        psychical = self.Int() + self.Wit() + self.Res()
        social = self.Pre() + self.Man() + self.Com()
        
        maximum = max(physical, psychical, social)
        minimum = min(physical, psychical, social)
        middle = physical + psychical + social - minimum - maximum
        
        return maximum - 5 - 3, middle - 4 - 3, minimum - 3 - 3       


    def academics(self): 
        return self.__academics
        
    def computer(self): 
        return self.__computer
        
    def crafts(self): 
        return self.__crafts
        
    def investigation(self): 
        return self.__investigation
        
    def medicine(self): 
        return self.__medicine
        
    def occult(self): 
        return self.__occult
        
    def politics(self): 
        return self.__politics
        
    def science(self):
        return self.__science
        
    def athletics(self): 
        return self.__athletics
        
    def brawl(self): 
        return self.__brawl
        
    def drive(self): 
        return self.__drive
        
    def firearms(self): 
        return self.__firearms
        
    def larceny(self): 
        return self.__larceny
        
    def stealth(self): 
        return self.__stealth
        
    def survival(self): 
        return self.__survival
        
    def weaponry(self):
        return self.__weaponry
        
    def animal_ken(self): 
        return self.__animal_ken
        
    def empathy(self): 
        return self.__empathy
        
    def expression(self): 
        return self.__expression
        
    def intimidation(self): 
        return self.__intimidation
        
    def persuasion(self): 
        return self.__persuasion
        
    def socialize(self): 
        return self.__socialize
        
    def streetwise(self): 
        return self.__streetwise
        
    def subterfuge(self):
        return self.__subterfuge
        


if __name__ == "__main__":

    sk = Skills()
    
    print(
        sk.academics(), sk.computer(), sk.crafts(), sk.investigation(), 
        sk.medicine(), sk.occult(), sk.politics(), sk.science(),
        sk.athletics(), sk.brawl(), sk.drive(), sk.firearms(), sk.larceny(), 
        sk.stealth(), sk.survival(), sk.weaponry(), sk.animal_ken(), 
        sk.empathy(), sk.expression(), sk.intimidation(), sk.persuasion(), 
        sk.socialize(), sk.streetwise(), sk.subterfuge()            
        )

