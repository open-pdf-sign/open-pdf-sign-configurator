def installMenu(info):
    # Create the menu
    print("Which names would you like to activate PDF signing for?")
    print("------------------------------------------------------------")
    i = 1
    for name in info:
        print(str(i) + ":", name["host"])
        i += 1
    print("------------------------------------------------------------")
    print(
        "Select the appropriate numbers separated by commas or leave input blank to select all options shown (Enter 'c' to cancel):")
    x = input()
    if x == "c": return
    optionsInt = list(range(len(info)))
    if x != "":
        options = x.split(",")
        try:
            optionsInt = [int(o) - 1 for o in options]
        except:
            print("didn't recognize input")

    if len(set(optionsInt)) is not len(optionsInt):
        print("multiple selections")
    for o in optionsInt:
        if o < 0 or o >= len(info):
            print(o+1, "out of range")
            return []
    options = [info[o] for o in optionsInt]
    return options
