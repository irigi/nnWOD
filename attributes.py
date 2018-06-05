import numpy as np
import matplotlib.pyplot as plt
from dicepool import dpool

class Attributes(object):
    """
    Class holding the attributes of a character
    """
    def __init__(self, Int=2, Wit=2, Com=2, Str=2, Dex=2, Sta=2, Man=2, Pre=2, Res=2):
        self.__int = Int
        self.__wit = Wit
        self.__com = Com

        self.__str = Str
        self.__dex = Dex
        self.__sta = Sta

        self.__man = Man
        self.__pre = Pre
        self.__res = Res

    def missing(self):
        '''
        Returns number of attributes that are missing for the character to be complete
        in order of maxima, middle and minimal category
        '''

        physical = self.Str() + self.Dex() + self.Sta()
        psychical = self.Int() + self.Wit() + self.Res()
        social = self.Pre() + self.Man() + self.Com()

        maximum = max(physical, psychical, social)
        minimum = min(physical, psychical, social)
        middle = physical + psychical + social - minimum - maximum

        return maximum - 5 - 3, middle - 4 - 3, minimum - 3 - 3

    def Str(self):
        return self.__str

    def Int(self):
        return self.__int

    def Dex(self):
        return self.__dex

    def Sta(self):
        return self.__sta

    def Wit(self):
        return self.__wit

    def Res(self):
        return self.__res

    def Com(self):
        return self.__com

    def Pre(self):
        return self.__pre

    def Man(self):
        return self.__man


if __name__ == "__main__":

    att = Attributes()

    print (att.missing())
    print (att.Man())

    print(att.Str(), att.Dex(), att.Sta())
    print(att.Int(), att.Wit(), att.Res())
    print(att.Pre(), att.Man(), att.Com())
