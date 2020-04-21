from os import listdir
from os.path import isfile
import pickle

from .pieces import *
from saves import *


class SaveLoadNew(ABC):
    def __init__(self):
        self.save_files = [s for s in listdir("saves/games")]

    def prompt_load(self):
        print("\nI found these save files:\n")
        for save in self.save_files:
            print(" - ", save)
        print("\nEnter one of these names or type a new one to start at the beginning.\n")

    def load_game(self, player_name):
        print("Loading save file for", player_name)
        storyline = Storyline()  # TODO: unserialize this from save file
        storyline.player.name = player_name  # temporary until previous line dev complete
        return storyline

    def new_game(self, player_name):
        print("Starting new game as ", player_name)
        storyline = Storyline()
        storyline.player.name = player_name
        return storyline


    #def save_progress(self, aasdas):
