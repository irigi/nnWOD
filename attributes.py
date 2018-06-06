import numpy as np
import matplotlib.pyplot as plt
from dicepool import dpool

class Attributes(object):
    """
    Class holding the attributes of a character
    """
    def __init__(self, Int=1, Wit=1, Com=1, Str=1, Dex=1, Sta=1, Man=1, Pre=1, Res=1):
        self.attr = {}
        self.attr['int'] = Int
        self.attr['wit'] = Wit
        self.attr['com'] = Com

        self.attr['str'] = Str
        self.attr['dex'] = Dex
        self.attr['sta'] = Sta

        self.attr['man'] = Man
        self.attr['pre'] = Pre
        self.attr['res'] = Res

        self.list = {}
        self.list['physical'] = ['str', 'dex', 'sta']

        self.list['psychical'] = ['int', 'wit', 'com']

        self.list['social'] = ['man', 'pre', 'res']

    def missing(self):
        '''
        Returns number of attributes that are missing for the character to be complete
        in order of maxima, middle and minimal category
        '''

        physical = self.get_sum_physical()
        psychical = self.get_sum_psychical()
        social = self.get_sum_social()

        maximum = max(physical, psychical, social)
        minimum = min(physical, psychical, social)
        middle = physical + psychical + social - minimum - maximum

        return maximum - 5 - 3, middle - 4 - 3, minimum - 3 - 3

    def finish(self):
        for key in self.list:
            while self.get_sum(name=key) < 3+3:
                sk = np.random.choice(self.list[key])
                self.attr[sk] = self.attr[sk] + 1


        rem = []
        for key in self.list:
            if self.get_sum(key) == 3+3:
                rem.append(key)
            else:
                print(key, self.get_sum(key))

        selected = np.random.choice(rem)

        remaining = [key for key in self.list]
        remaining.remove(selected)

        for key in remaining:
            while self.get_sum(name=key) < 4+3:
                sk = np.random.choice(self.list[key])
                self.attr[sk] = self.attr[sk] + 1


        rem = []
        for key in remaining:
            if self.get_sum(key) == 4+3:
                rem.append(key)

        selected = np.random.choice(rem)
        remaining.remove(selected)

        for key in remaining:
            while self.get_sum(name=key) < 5+3:
                sk = np.random.choice(self.list[key])
                self.attr[sk] = self.attr[sk] + 1

    def get_sum(self, name):
        return sum([self.attr[key] for key in self.list[name]])

    def get_sum_psychical(self):
        return self.get_sum('psychical')

    def get_sum_physical(self):
        return self.get_sum('physical')

    def get_sum_social(self):
        return self.get_sum('social')

    def attribute(self, attribute):
        return self.attr[attribute]


if __name__ == "__main__":

    att = Attributes()

    print (att.missing())
    att.finish()
    print (att.missing())

    print(att.attribute('str'), att.attribute('dex'), att.attribute('sta'))
    print(att.attribute('int'), att.attribute('wit'), att.attribute('res'))
    print(att.attribute('pre'), att.attribute('man'), att.attribute('com'))
