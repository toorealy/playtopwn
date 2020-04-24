from playtopwn.saveload import *
from playtopwn.pieces import *
from playtopwn.actions import *
from playtopwn.prompt import user_prompt


def game_loop(player):
    try:
        while True:
            print('\nSelect one of these options:\n')
            choice = user_prompt(player.story, player.actions)
            if choice is not None:
                player.actions[choice].execute()
    except KeyboardInterrupt:
        player.story.save()
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
