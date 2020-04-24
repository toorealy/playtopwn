def user_prompt(story, actions: list):
    str_actions = []
    for action in actions:
        str_actions.append(str(action))
        print("[", action,"]")
    prompt = str(input("\n {} # ".format(story.name)))
    print("\n\n\n\n*****************************************************************************************\n\n")
    candidates = [str_actions.index(elem) for elem in str_actions if prompt.lower() in elem.lower()]
    if prompt.lower() in str_actions:
        return str_actions.index(prompt.lower())
    elif len(candidates) == 1:
        return candidates[0]
    elif len(candidates) > 1:
        #print("\nThat was ambiguous\n")
        return None
    else:
        #print("\nI didn't understand that command.\n")
        return None
