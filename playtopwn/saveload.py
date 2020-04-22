from os import listdir
import pickle

from .pieces import *
from saves import *


def save_object(object, dest_file):
    with open(dest_file, 'w') as out_file:
        json.dump(dict(object), out_file)

def show_saves(folder: str) -> list:
    return [s for s in listdir("saves/" + folder)]


def load_object(src_file):
    filehandler = open(src_file, 'r')
    return json.load(filehandler)


class SaveLoadNew(ABC):
    def __init__(self):
        self.save_files = [s for s in listdir("saves/challenges")]

    def prompt_load(self):
        print("\nI found these save files:\n")
        for save in self.save_files:
            print(" - ", save)
        print("\nEnter one of these names or type a new one to start at the beginning.\n")

    def load_game(self, challenge):
        print("\nLoading save file for", challenge)
        challenge = HackChallenge()  # temporary until previous line dev complete
        return challenge.load(challenge)

    def new_game(self, challenge):
        print("\nStarting new challenge ", challenge)
        challenge = HackChallenge()
        challenge.name = challenge
        return challenge


    #def save_progress(self, aasdas):
