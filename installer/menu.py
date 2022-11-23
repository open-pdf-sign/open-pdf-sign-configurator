def installMenu(installers):
    # Create the menu
    print("Which names would you like to activate PDF signing for?")
    print("------------------------------------------------------------")
    i = 1
    infos = []
    offsets = []
    for installer in installers:
        info = installer.getNginxInfo()
        for entry in info:
            print(str(i) + ":", " ".join(entry["host"]))
            i += 1
        offsets.append(i-1)
        infos.append(info)
    print("------------------------------------------------------------")
    print(
        "Select the appropriate numbers separated by commas or leave input blank to select all options shown (Enter 'c' to cancel):")
    userInput = input()
    if userInput == "c": return
    optionsInt = list(range(i-1))
    if userInput != "":
        options = userInput.split(",")
        try:
            optionsInt = [int(o) - 1 for o in options]
        except:
            print("didn't recognize input")

    if len(set(optionsInt)) is not len(optionsInt):
        print("multiple selections")
        return [], []
    for o in optionsInt:
        if o < 0 or o >= i:
            print(o + 1, "out of range")
            return [], infos
    selection = [[] for _ in range(len(infos))]
    for i in optionsInt:
        j = 0
        for offset in offsets:
            if i < offset:
                if j > 0:
                    selection[j].append(i - offsets[j - 1])
                else:
                    selection[j].append(i)
                break
            j += 1

    return selection, infos
