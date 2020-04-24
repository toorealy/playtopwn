from abc import ABC
import os

from playtopwn.prompt import user_prompt


class Player(ABC):
    """ This class houses the entire game. It is from this class that
    the player proceeds to interact with the environment
    """
    def __init__(self, story):
        self.name = 'player1'
        a1 = FileMenu(story)
        a2 = Findings(story)
        self.actions = [a1, a2]
        self.findings = []
        self.story = story

    def __dict__(self):
        return {'name':str(self.name)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def delete_save(self, category, file):
        dlt_file = "src/saves/" + category + "/" + file
        if os.path.isfile(dlt_file):
            print(os.path.isfile(dlt_file), dlt_file)
            os.remove(dlt_file)
        else:
            print("  ", file, "doesn't exist to delete.")

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
    """ Base class for actions the player will be able to do.
    Each 'execute' block should be overriden to provide a scene
    in the game.
    """
    def __init__(self, story):
        self.name = None
        self.story = story

    def __str__(self):
        return self.name

    def __dict__(self):
        return {'name':str(self.name)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def execute(self):
        """ Override this method to get unique action
        However, this general template should be followed"""
        print("\nYou have reached the PlayerAction master class.\n")
        actions = ['whip', 'nae nae', 'back']
        user_prompt(self.story, actions)

    def back(self):
        """Each action class should include the option for 'back' in
        their list of actions"""
        pass


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


class FileMenu(PlayerAction):
    def __init__(self, story):
        self.name = "file menu"
        self.story = story

    def execute(self):
        print("\nFile Menu\n")
        actions = ['delete challenge', 'save progress', 'back']
        choice = user_prompt(self.story, actions)
        if choice is not None:
            if choice == 0:
                self.delete_challenge()
            if choice == 1:
                self.save_progress()

    def delete_challenge(self):
        saves = self.story.show_saves()
        print("- [none]\n\nWhich would you like to delete?\n")
        choice = user_prompt(self.story, saves)
        if choice is not None:
            dlt_file = "src/saves/challenges/" + saves[choice]
            if os.path.isfile(dlt_file):
                os.remove(dlt_file)
                print("'", dlt_file, "' was deleted.")
            else:
                print("  ", file, "doesn't exist to delete.")
        self.execute()  #  This should be at the end of each action except 'back'


    def save_progress(self):
        self.story.save()


class Findings(PlayerAction):
    def __init__(self, story):
        self.name = "examine findings"
