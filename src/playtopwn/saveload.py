from os import listdir
import pickle

from .pieces import *


class SaveLoadNew(ABC):
    def __init__(self):
        self.save_files = [s for s in listdir("src/saves/challenges")]

    def prompt_load(self):
        print("\nI found these saved challenges:\n")
        for save in self.save_files:
            print(" - ", save)
        print("\nEnter one of these challenge names or type a new one.\n")

    def load_game(self, challenge) -> HackChallenge:
        print("\nLoading save file for", challenge)
        challenge_obj = HackChallenge()  # temporary until previous line dev complete
        return challenge_obj.load(challenge)

    def new_game(self, challenge: str) -> HackChallenge:
        print("\nStarting new challenge ", challenge)
        challenge_obj = HackChallenge()
        challenge_obj.name = challenge
        return challenge_obj
