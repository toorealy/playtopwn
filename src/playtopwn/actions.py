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
        a2 = ModSystems(story)
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
        action_dict = {}
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

"""Menus should be classes
End-of-line commands should be functions of those classes
"""
class FileMenu(PlayerAction):
    def __init__(self, story):
        self.name = "file menu"
        self.story = story

    def execute(self):
        print("\nFile Menu\n")
        actions = ['delete challenge', 'save progress', 'back']
        action_dict = {
            0 : self.delete_challenge,
            1 : self.save_progress,
            2 : self.back
        }
        choice = user_prompt(self.story, actions)
        if choice is not None:
            action_dict.get(choice)()
        else:
            self.execute()

    def delete_challenge(self):
        saves = self.story.show_saves(silent=True)
        print("\nWhich would you like to delete?\n")
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
        self.execute()  #  This should be at the end of each action except 'back'


class ModSystems(PlayerAction):
    def __init__(self, story):
        self.name = "systems"
        self.story = story

    def execute(self):
        print("\nSystems Menu\n")
        actions = ['display systems', 'add system', 'remove system', 'back']
        action_dict = {
            0 : self.display_systems,
            1 : self.add_system,
            2 : self.remove_system,
            3 : self.back
        }
        choice = user_prompt(self.story, actions)
        if choice is not None:
            action_dict.get(choice)()
        else:
            self.execute()  #  This should be at the end of each action except 'back'

    def display_systems(self):
        print("\nThese are the systems so far:\n")
        self.story.show_systems()
        self.execute()  #  This should be at the end of each action except 'back'

    def add_system(self):
        print("\nWhat is the name of the new system?\n")
        sys_name = str(input("Name: "))
        self.story.add_system(sys_name)
        self.execute()  #  This should be at the end of each action except 'back'

    def remove_system(self):
        print("\nWhich system would you like to remove?\n")
        choice = user_prompt(self.story, self.story.show_systems(silent=True))
        if choice is not None:
            print("\nSystem ", self.story.systems.pop(choice)['name'], " deleted.")
        self.execute()  #  This should be at the end of each action except 'back'
