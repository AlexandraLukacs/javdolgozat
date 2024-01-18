def szinek():
    szin: str= str(input("\tKérek egy színkeverési módszert: "))
    kod: str= str(input("\tKérem a kódot: "))
    if szin == "RGB":
        if 5 <= len(kod) <= 11:
            print("\tMegfelelő hossz.")
        else:
            print("\tNem megfelelő hossz.")
    elif szin == "HEX":
        if len(kod) <= 6:
            print("\tMegfelelő hossz.")
        else:
            print("\tNem megfelelő hossz.")
    elif szin == "HSL":
        if 7 <= len(kod) <= 13:
            print("\tMegfelelő hossz.")
        else:
            print("\tNem megfelelő hossz.")
    else:
        print("\tBonyolult kiszámolni")