from os import listdir
import pickle

from .pieces import *
#from saves import *




class SaveLoadNew(ABC):
    def __init__(self):
        self.save_files = [s for s in listdir("src/saves/challenges")]

    def prompt_load(self):
        print("\nI found these save files:\n")
        for save in self.save_files:
            print(" - ", save)
        print("\nEnter one of these names or type a new one to start at the beginning.\n")

    def load_game(self, challenge):
        print("\nLoading save file for", challenge)
        challenge_obj = HackChallenge()  # temporary until previous line dev complete
        return challenge_obj.load(challenge)

    def new_game(self, challenge):
        print("\nStarting new challenge ", challenge)
        challenge = HackChallenge()
        challenge.name = challenge
        return challenge


    #def save_progress(self, aasdas):
