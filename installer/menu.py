def installMenu(info):
    # Create the menu
    print("Which names wowuld you like to activate PDF signing for?")
    print("------------------------------------------------------------")
    i = 1
    for name in info:
        print(str(i) + ":", name["server_name"])
        i += 1
    print("------------------------------------------------------------")
    print(
        "Select the appropriate numbers separated by commas or leave input blank to select all options shown (Enter 'c' to cancel):")
    x = input()
    if x == "c": return
    if x != "":
        options = x.split(",")
        try:
            options = [info[int(o) - 1] for o in options]

        except:
            print("didn't recognize input")
        return options
