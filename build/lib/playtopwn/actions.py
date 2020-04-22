from abc import ABC


class Player(ABC):
    def __init__(self, story):
        self.name = 'player1'
        a1 = Character(story)
        a2 = Findings(story)
        self.actions = [a1, a2]
        self.findings = []
        self.story = story

    def __dict__(self):
        return {'name':str(self.name)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class PlayerAction(ABC):
    def __init__(self, story):
        self.name = None

    def __str__(self):
        return self.name

    def __dict__(self):
        return {'name':str(self.name)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def execute(self, story):
        print("I am the effect of {}".format(self.name))


    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class Character(PlayerAction):
    def __init__(self, story):
        self.name = "configure character"



class Findings(PlayerAction):
    def __init__(self, story):
        self.name = "examine findings"
