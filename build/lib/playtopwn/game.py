from playtopwn.saveload import *
from playtopwn.pieces import *
from playtopwn.actions import *

#PROMPT = ""


def game_loop(player):
    try:
        while True:
            print('\nSelect one of these options:\n')
            str_actions = []
            for action in player.actions:
                str_actions.append(action.name)
                print("[", action.name,"]")
            prompt = str(input("{} # ".format(player.story.name)))
            print("\n\n\n\n*****************************************************************************************\n\n")
            candidates = [str_actions.index(elem) for elem in str_actions if prompt.lower() in elem]#[str_actions.index(action) for action in str_actions if prompt.lower() in action.lower()]
            if len(candidates) == 1:
                player.actions[candidates[0]].execute(player.story)
            elif len(candidates) > 1:
                print("\nThat was an ambiguous command.\n")
            else:
                print("\nI didn't understand that command.\n")
    except KeyboardInterrupt:
        print("\nGoodbye.")

def the_beginning():
    story = game_init()
    player = Player(story)
    if player.story:
        print("\nSo there you were...\n")
        game_loop(player)
    else:
        while not player.story:
            print("\nPlease enter a name\n")
            player.story = game_init()
        game_loop(player)

def game_init():
    """ Starts the game by loading a previous game or creating a new one"""
    try:
        saves = SaveLoadNew()
        saves.prompt_load()
        user_says = str(input(" # "))
        if user_says in saves.save_files:
            story = saves.load_game(user_says)
        elif user_says:
            story = saves.new_game(user_says)
        else:
            story = None
        return story
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    the_beginning()
