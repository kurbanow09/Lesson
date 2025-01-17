isgarler = { "Anna" : {"synag1" : 79,
                        "synag2" : 13,
                        "synag3" : 29},

            "Merdan" : {"synag1" : 78,
                    "synag2" : 19,
                    "synag3" : 66},

            "Oraz" : {"synag1" : 56,
                    "synag2" : 100,
                    "synag3" : 57},
}

ady = input('Ady: ')
if ady in isgarler:
    isleg = input('Doly maglumat:(howa/yok) ')
    if isleg == "howa":
        print(isgarler[ady])
    else:
        mag = input('synag1/synag2/synag3 ')
        print(isgarler[ady][mag])
else:
    print(f"{ady} atly isgar yok")
