from .actions import *
from .pieces import *

def the_beginning():
    story = game_init()
    print("\nSo there you were...\n")



def game_init() -> Storyline:
    """ Starts the game by loading a previous game or creating a new one"""
    saves = SaveLoadNew()
    saves.prompt_load()
    user_says = str(input("#"))
    if user_says in saves.save_files:
        story = saves.load_game(user_says)
    else:
        story = saves.new_game(user_says)
    return story

if __name__ == "__main__":
    the_beginning()
